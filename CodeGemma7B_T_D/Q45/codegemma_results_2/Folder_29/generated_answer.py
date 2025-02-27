def palindromes_between_indices(s):
    return {''.join(word) for word in itertools.permutations(sorted([c.lower() for c in s[2:10]]))} if len(s) >= 6 else set()