from itertools import permutations

def palindromes_between_indices(s):
    letters = set(s[:4].lower())
    palindromes = set()
    for r in range(3, 5):
        for p in permutations(letters, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes