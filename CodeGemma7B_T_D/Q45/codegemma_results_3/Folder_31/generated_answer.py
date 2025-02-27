from itertools import permutations

def palindromes_between_indices(s):
    t = s[1:9].lower()
    return set([p for p in permutations(t) if p[0] in 'aeiou' and p[-1] in 'aeiou' and (p[2:6] == p[-3:-1:-1])])