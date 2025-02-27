import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:9] if c.isalpha()]
    if len(letters) >= 4:
        permutations = set(itertools.permutations(letters))
        palindromes = {''.join(p[:len(p) // 2] + p[len(p) // 2 - 1::-1]) for p in permutations if len(p) >= 4}
        return {p for p in palindromes if p == p[::-1]}
    return set()