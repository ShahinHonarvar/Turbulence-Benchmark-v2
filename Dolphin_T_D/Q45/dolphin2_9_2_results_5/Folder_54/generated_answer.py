def palindromes_between_indices(s):
    s = s[4:10]
    s = ''.join([c for c in s if c.isalpha()])
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes