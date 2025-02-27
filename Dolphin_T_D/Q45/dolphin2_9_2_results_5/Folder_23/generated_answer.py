from itertools import combinations

def palindromes_between_indices(s):
    s = s[:7].lower()
    res = set()
    for i in range(4, len(s) + 1):
        palindromes = [''.join(q) for q in combinations(s, i) if ''.join(q) == ''.join(reversed(''.join(q)))]
        res.update(palindromes)
    return res