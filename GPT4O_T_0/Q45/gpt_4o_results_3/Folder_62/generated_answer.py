from itertools import permutations

def palindromes_between_indices(s):
    s = s[:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 7):
        if perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return palindromes