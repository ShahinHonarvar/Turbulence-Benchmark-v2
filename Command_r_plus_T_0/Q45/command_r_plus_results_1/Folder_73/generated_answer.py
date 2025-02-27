def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substring = s[3:7].lower()
    substring_letters = set(substring)
    if substring_letters.issubset(english_letters):
        for i in range(len(substring)):
            for j in range(i + 3, len(substring) + 1):
                palindrome = substring[i:j]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes