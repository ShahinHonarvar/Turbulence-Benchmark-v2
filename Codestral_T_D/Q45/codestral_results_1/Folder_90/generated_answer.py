from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:6].lower()
    length = len(s)
    palindromes = set()
    for i in range(4, length + 1):
        for p in permutations(s, i):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes