def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for start in range(n - 278):
        for end in range(start + 279, n + 1):
            substring = s[start:end]
            if len(substring) == 279 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes