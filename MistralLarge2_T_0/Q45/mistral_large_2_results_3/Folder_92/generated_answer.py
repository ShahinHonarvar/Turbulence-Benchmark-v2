import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:8] if c.isalpha()]
    permutations = set((''.join(p) for i in range(4, len(letters) + 1) for p in itertools.permutations(letters, i)))
    palindromes = {p for p in permutations if p == p[::-1] and len(p) >= 4}
    return palindromes