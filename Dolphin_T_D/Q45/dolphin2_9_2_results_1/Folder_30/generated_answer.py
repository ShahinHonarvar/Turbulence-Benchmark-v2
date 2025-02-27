from itertools import permutations

def palindromes_between_indices(string):
    s = string[0:5].lower()
    palindromes = set()
    for i in range(4, len(s) + 1):
        for p in permutations(s, i):
            t = ''.join(p)
            p = t[::-1]
            if s in t and t == p:
                palindromes.add(t)
    return palindromes