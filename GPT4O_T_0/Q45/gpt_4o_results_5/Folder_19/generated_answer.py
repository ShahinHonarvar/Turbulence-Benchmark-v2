from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        if perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return {p for p in palindromes if len(p) >= 7}