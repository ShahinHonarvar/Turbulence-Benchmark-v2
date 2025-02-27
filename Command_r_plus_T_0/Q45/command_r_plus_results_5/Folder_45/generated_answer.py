def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substring = s[5:10].lower()
    substring_letters = set(substring)
    if substring_letters.issubset(english_letters):
        for i in range(6):
            for j in range(i + 4, 10):
                if substring[i] == substring[j]:
                    palindrome = substring[i:j + 1]
                    if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes