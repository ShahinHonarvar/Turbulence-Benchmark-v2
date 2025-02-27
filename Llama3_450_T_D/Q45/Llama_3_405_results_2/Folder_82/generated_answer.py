import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:7] if c.isalpha() and c.lower() in 'abcdefghijklmnopqrstuvwxyz']
    letters = ''.join(letters).lower()
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for combo in itertools.combinations(letters, r):
            for perm in itertools.permutations(combo):
                p = ''.join(perm)
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes