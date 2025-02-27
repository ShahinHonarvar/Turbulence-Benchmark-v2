def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substring = s[5:10].lower()
    substring_letters = set(substring)
    if substring_letters.issubset(english_letters):
        for i in range(6):
            for j in range(i + 4, 10):
                substring_palindrome = substring[i:j]
                if substring_palindrome == substring_palindrome[::-1]:
                    palindromes.add(substring_palindrome)
    return palindromes