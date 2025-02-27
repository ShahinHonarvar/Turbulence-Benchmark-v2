from itertools import permutations

def palindromes_between_indices(s):
    s = s[8:10].lower()
    palindromes = set()
    for p in permutations(s, len(s)):
        if len(p) >= 3 and p == p[::-1]:
            palindromes.add(''.join(p))
    return palindromes