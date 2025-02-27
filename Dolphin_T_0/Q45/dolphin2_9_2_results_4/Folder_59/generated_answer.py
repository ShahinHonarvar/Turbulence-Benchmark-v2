from itertools import permutations

def palindromes_between_indices(s):
    substring = s[8:10]
    palindromes = set()
    for p in permutations(substring, length=3):
        if ''.join(p).lower() == ''.join(reversed(p)).lower():
            palindromes.add(''.join(p))
    return palindromes