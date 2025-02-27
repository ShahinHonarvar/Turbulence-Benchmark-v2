from itertools import permutations, chain

def palindromes_between_indices(s):
    letters = [c for c in s[1:6] if c.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for p in chain(*map(lambda x: permutations(x, len(x)), range(6, 0, -1))):
        if p == p[::-1]:
            palindromes.add(''.join(p))
    return palindromes