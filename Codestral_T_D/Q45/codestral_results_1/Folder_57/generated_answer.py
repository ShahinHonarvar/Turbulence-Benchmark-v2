from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6].lower()
    palindromes = set()
    for i in range(5, 0, -1):
        for p in permutations(s, i):
            if i > 1 and p[0] == p[-1] and (p == p[::-1]):
                palindromes.add(''.join(p))
    return palindromes