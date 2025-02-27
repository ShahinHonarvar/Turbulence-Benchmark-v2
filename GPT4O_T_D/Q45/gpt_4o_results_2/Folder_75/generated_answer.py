from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [ch for ch in s[2:5] if ch.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        if perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return palindromes