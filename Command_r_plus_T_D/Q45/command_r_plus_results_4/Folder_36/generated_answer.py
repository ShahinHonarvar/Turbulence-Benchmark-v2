def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substring = ''.join(filter(english_letters.__contains__, s[5:9]))
    for i in range(len(substring) - 2):
        for j in range(i + 2, len(substring) + 1):
            palindrome = substring[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes