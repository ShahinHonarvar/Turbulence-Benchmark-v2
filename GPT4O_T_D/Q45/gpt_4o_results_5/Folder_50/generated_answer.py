from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    chars = [ch.lower() for ch in s[4:9] if ch.isalpha()]
    if len(chars) < 5:
        return set()
    palindromes_set = set()
    for perm in permutations(chars):
        if perm == perm[::-1]:
            palindromes_set.add(''.join(perm))
    return palindromes_set