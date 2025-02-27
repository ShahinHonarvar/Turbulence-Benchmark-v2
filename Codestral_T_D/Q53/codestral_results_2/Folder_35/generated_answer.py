def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) >= 26:
                palindromes.add(sub)
    return palindromes