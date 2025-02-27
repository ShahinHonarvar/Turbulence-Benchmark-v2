def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join((c for c in s if c.isalpha()))
    n = 42
    palindromes = set()
    for length in range(n, len(s) + 1):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes