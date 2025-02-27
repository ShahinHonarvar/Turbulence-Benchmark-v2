def palindromes_between_indices(word):
    return {''.join(p) for p in permutations(word[8:10].lower(), r=len(word[8:10])) if p[0] >= p[1]}