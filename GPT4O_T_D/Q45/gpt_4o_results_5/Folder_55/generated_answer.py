from itertools import permutations

def palindromes_between_indices(s):
    s = s[:3].lower()
    letters = ''.join([ch for ch in s if ch.isalpha()])
    palindromes = set()
    for perm in set(permutations(letters)):
        perm = ''.join(perm)
        if len(perm) >= 3 and perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes