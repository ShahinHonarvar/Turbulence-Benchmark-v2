import itertools

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[2:10] if c.isalpha()]
    palindromes = set()
    for r in range(7, len(chars) + 1):
        for p in itertools.permutations(chars, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes