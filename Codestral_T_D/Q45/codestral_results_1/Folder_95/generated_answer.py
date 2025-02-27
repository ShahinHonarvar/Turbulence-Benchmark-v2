from itertools import permutations

def palindromes_between_indices(s):
    s_slice = s[7:9].lower()
    palindromes = set()
    for r in range(3, len(s_slice) + 1):
        for perm in permutations(s_slice, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes