from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        if len(perm) >= 6 and perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return palindromes