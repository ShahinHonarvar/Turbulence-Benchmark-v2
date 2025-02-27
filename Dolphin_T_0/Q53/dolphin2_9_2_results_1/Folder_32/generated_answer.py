def palindrome_of_length_at_least_n(s):
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 69, n):
            sub = s[i:j + 1]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes