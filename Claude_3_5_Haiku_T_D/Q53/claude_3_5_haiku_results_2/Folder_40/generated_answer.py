def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for length in range(3, n + 1):
        for start in range(n - length + 1):
            substr = s[start:start + length]
            if len(substr) >= 3 and all((c.isalpha() for c in substr)):
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes