import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:7] if c.isalpha() and c.lower() in 'abcdefghijklmnopqrstuvwxyz']
    letters = [c.lower() for c in letters]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes