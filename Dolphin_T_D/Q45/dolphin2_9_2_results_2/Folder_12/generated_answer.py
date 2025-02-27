from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:9].lower()
    palindromes = {''.join(p) for p in permutations(s) if len(p) >= 4}
    return {p for p in palindromes if p == p[::-1]}