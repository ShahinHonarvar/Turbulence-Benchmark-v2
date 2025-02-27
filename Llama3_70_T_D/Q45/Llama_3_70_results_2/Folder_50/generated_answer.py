from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    s = ''.join(filter(str.isalpha, s))
    if len(s) < 5:
        return set()
    palindromes = set((''.join(p) for p in permutations(s) if len(p) >= 5 and p == p[::-1]))
    return palindromes