def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 5, n):
            substr = s[i:j + 1]
            if substr == substr[::-1] and len(substr) >= 6:
                palindromes.add(substr)
    return palindromes