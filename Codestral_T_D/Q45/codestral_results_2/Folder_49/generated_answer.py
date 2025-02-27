from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:8].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for p in permutations(s, i):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes