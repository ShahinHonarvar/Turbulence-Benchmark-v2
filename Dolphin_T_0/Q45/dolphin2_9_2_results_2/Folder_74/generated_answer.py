from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7]
    s = ''.join(filter(str.isalpha, s)).lower()
    if len(set(s)) < 5:
        return set()
    palindromes = set()
    for p in permutations(s, len(s)):
        if ''.join(p) == ''.join(p[::-1]):
            palindromes.add(''.join(p))
    return palindromes