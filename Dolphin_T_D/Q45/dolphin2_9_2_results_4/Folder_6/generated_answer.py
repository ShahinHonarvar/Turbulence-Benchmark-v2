def palindromes_between_indices(s):
    s = s[:8].lower()
    s = ''.join(filter(str.isalpha, s))
    if len(s) < 2:
        return set()
    pal = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                pal.add(sub)
    return pal