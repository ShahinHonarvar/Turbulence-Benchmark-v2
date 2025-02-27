import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:3] if c.isalpha()]
    permutations = [''.join(p) for p in itertools.permutations(letters, 3) if p != p[::-1]]
    palindromes = [p for p in permutations if p.lower() == p[::-1].lower()]
    return set(palindromes)