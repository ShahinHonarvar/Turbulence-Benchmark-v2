def palindrome_of_length_at_least_n(s):
    s = ''.join((c for c in s if c.isalpha())).lower()
    n = len(s)
    palindromes = set()
    for start in range(n):
        for end in range(start + 34, n):
            substring = s[start:end + 1]
            if substring == substring[::-1] and len(substring) >= 35:
                palindromes.add(substring)
    return palindromes