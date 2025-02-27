def palindromes_between_indices(s):
    chars = set(s[2:7].lower())
    palindromes = set()
    for char in chars:
        for p in [''.join(p) for p in itertools.permutations(chars, 3) if p[0] == p[-1]]:
            palindromes.add(p)
    return palindromes