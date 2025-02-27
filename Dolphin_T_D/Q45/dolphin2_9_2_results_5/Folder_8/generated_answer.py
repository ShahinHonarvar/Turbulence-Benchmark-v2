from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:6] if c.isalpha()]
    if len(letters) < 2:
        return set()
    palindromes = set()
    for p in permutations(letters, len(letters)):
        if len(p) < 2:
            continue
        pal = ''.join(p).lower()
        if pal == pal[::-1]:
            palindromes.add(pal)
    return palindromes