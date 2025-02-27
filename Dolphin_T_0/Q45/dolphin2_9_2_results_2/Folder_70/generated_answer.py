def palindromes_between_indices(s):
    pal = set()
    for i in range(1, 7):
        for j in range(i + 2, 7):
            sub = s[i:j]
            sub = ''.join(filter(str.isalpha, sub)).lower()
            if len(sub) >= 4:
                for p in set(sub):
                    pal.add(p)
    return pal