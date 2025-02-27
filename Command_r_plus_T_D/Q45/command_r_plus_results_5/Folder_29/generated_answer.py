def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    substring = s[2:10]
    substring_letters = set(substring)
    if substring_letters.issubset(english_letters):
        for i in range(3, 8):
            for j in range(i + 1, 10):
                substring_palindrome = substring[i:j]
                if substring_palindrome == substring_palindrome[::-1] and len(substring_palindrome) >= 6:
                    palindromes.add(substring_palindrome)
    return palindromes