from itertools import permutations

def palindromes_between_indices(s):
    letters = sorted([x for x in s[3:8] if x.isalpha()])
    return set((''.join(p) for p in permutations(letters) if len(p) >= 4 and ''.join(p).lower() == ''.join(p)[::-1].lower()))