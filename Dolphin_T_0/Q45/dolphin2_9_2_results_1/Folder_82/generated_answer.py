from itertools import permutations
    import re

def palindromes_between_indices(s):
    string = s[1:7]
    letters = ''.join(sorted(set(re.findall('[a-zA-Z]', string))))
    palindromes = set()
    for p in permutations(letters, 7):
        p = ''.join(p)
        if p == p[::-1] and len(p) >= 7:
            palindromes.add(p)
    return palindromes