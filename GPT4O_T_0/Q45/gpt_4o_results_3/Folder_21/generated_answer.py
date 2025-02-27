from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        if perm == perm[::-1] and len(perm) >= 7:
            palindromes.add(''.join(perm))
    return palindromes