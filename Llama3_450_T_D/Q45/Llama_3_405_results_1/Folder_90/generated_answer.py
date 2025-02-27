import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:6] if c.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for t in itertools.permutations(letters, r):
            p = ''.join(t)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes