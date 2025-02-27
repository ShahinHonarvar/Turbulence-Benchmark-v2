def palindromes_between_indices(s):
    s = s[5:9].lower()
    letters = ''.join(filter(str.isalpha, s))
    result = set()
    for r in range(3, len(letters) + 1):
        for p in [''.join(p) for p in itertools.permutations(letters, r) if p == p[::-1]]:
            result.add(p)
    return result