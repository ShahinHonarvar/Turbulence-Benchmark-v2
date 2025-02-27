def palindromes_between_indices(s):
    s_sub = s[:8]
    s_sub = ''.join((c for c in s_sub if c.isalpha()))
    s_sub = ''.join((c.lower() for c in s_sub))
    subsets = itertools.chain.from_iterable((combinations(s_sub, r) for r in range(len(s_sub) + 1)))
    palindromes = set()
    for subset in subsets:
        subset = ''.join(sorted(tuple(subset)))
        if len(subset) >= 4 and subset == subset[::-1]:
            palindromes.add(subset)
    return palindromes