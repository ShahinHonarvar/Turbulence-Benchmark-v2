def palindromes_between_indices(s):
    return {p for p in (''.join(l) for l in itertools.permutations(''.join((c for c in s[2:9])), 4)) if p == p[::-1]}