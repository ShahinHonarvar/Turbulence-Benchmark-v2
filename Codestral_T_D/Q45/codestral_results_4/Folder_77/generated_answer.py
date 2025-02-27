from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:7].lower()
    palindromes = set()
    for perm in permutations(s, len(s)):
        perm = ''.join(perm)
        if len(perm) >= 4 and perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes