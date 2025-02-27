from itertools import combinations_with_replacement

def palindromes_between_indices(s):
    s = s[1:3].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for p in combinations_with_replacement(s, i):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes