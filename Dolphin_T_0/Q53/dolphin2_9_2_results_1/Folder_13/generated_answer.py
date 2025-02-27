def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 52
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(n, len(s) - i + 1):
            substring = s[i:i + j]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes