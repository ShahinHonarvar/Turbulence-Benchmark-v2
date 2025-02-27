def palindromes_between_indices(s):
    letters = set((s[i].lower() for i in range(3, 8) if s[i].isalpha()))
    if len(letters) < 3:
        return set()
    result = set()
    for c1 in letters:
        for c2 in letters:
            if c1 != c2:
                for c3 in letters:
                    if c3 != c1 and c3 != c2:
                        for p in ([c1, c2, c3, c2, c1], [c1, c3, c2, c3, c1], [c3, c1, c2, c1, c3], [c3, c2, c1, c2, c3]):
                            result.add(''.join(p))
    return result