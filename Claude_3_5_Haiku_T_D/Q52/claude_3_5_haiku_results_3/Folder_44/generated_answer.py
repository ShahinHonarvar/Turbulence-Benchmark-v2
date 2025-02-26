def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for start in range(n - 444):
        for end in range(start + 445, n + 1):
            substring = s[start:end]
            if len(substring) == 445 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes