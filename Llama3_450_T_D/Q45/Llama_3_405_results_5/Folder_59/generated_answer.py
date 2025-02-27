from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[8:10].lower()
    s = ''.join(filter(str.isalpha, s))
    if len(s) < 3:
        return set()
    counter = Counter(s)
    palindromes = set()
    for p in permutations(s):
        p = ''.join(p)
        if p == p[::-1] and len(p) >= 3:
            palindromes.add(p)
    return palindromes