def palindromes_between_indices(str):
    letters = set(str[1:4].lower())
    return {''.join(p) for p in itertools.product(*[letters] * len(str[1:4])) if p == p[::-1]}