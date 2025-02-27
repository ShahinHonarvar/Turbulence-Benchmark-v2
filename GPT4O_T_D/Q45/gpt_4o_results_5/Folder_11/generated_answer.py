from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:8].lower()
    letters = [ch for ch in substring if ch.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        if perm == perm[::-1]:
            palindromes.add(''.join(perm))
    return {p for p in palindromes if len(p) >= 4}