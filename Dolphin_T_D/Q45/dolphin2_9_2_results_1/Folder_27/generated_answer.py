def palindromes_between_indices(s):
    s = s[2:9]
    s = ''.join([c for c in s if c.isalpha()])
    s = s.lower()
    p = set()
    for i in range(6, len(s) + 1):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1]:
                p.add(s[j:j + i])
    return p