from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:7].lower()
    palindromes = set()
    for p in permutations(s):
        if len(p) >= 4 and p == p[::-1]:
            palindromes.add(''.join(p))
    return palindromes