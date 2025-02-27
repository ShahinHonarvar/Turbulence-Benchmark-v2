import itertools

def palindromes_between_indices(s):
    chars = [c for c in s[:3].lower() if c.isalpha()]
    palindromes = set()
    for r in range(3, len(chars) + 1):
        for perm in itertools.permutations(chars, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes