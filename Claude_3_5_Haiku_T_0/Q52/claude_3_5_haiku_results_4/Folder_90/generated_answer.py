def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 317):
        for j in range(i + 318, n + 1):
            substring = s[i:j]
            if len(substring) == 318 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes