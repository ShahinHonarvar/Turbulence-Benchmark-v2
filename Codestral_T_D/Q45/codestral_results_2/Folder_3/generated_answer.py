from itertools import permutations

def palindromes_between_indices(s):
    s = s[7:10].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for p in set(permutations(s, i)):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes