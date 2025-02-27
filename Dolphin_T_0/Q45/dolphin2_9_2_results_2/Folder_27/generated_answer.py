def palindromes_between_indices(s):
    pals = set()
    subset = s[2:9]
    letters = {c.lower(): s.count(c) for c in subset}
    for len_ in range(6, len(subset) + 1):
        for perm in itertools.permutations(letters.keys(), len_):
            if all((s[2:9].lower().count(c) >= letters[c] for c in perm)):
                pal = ''.join(perm)
                if pal == pal[::-1]:
                    pals.add(pal)
    return pals