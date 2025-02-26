def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = 138
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n - 1, len(s)):
            substr = s[i:j + 1]
            if len(substr) >= n and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes