def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for start in range(n - 28):
        for end in range(start + 29, n + 1):
            substring = s[start:end]
            if len(substring) == 29 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes