def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 15, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes