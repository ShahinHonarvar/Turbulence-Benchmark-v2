import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[5:10])).lower()
    permutations = set((''.join(p) for i in range(5, len(letters) + 1) for p in itertools.permutations(letters, i)))
    return {p for p in permutations if p == p[::-1] and len(p) >= 5}