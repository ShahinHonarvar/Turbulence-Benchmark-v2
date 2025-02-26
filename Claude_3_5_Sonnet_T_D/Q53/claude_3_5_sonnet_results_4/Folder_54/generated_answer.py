def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 74, n + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes