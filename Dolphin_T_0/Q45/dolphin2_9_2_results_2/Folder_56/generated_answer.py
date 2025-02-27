def palindromes_between_indices(S):
    S = ''.join(filter(str.isalpha, S[4:10]))
    return set(filter(lambda x: len(x) >= 5, {''.join(p) for p in permutations(S)}))