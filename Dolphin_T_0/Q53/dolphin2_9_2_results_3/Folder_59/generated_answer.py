def palindrome_of_length_at_least_n(s):
    s = ''.join((c for c in s.lower() if c.isalpha()))
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 1, length):
            sub = s[i:j + 1]
            if sub == sub[::-1] and len(sub) >= 20:
                palindromes.add(sub)
    return palindromes