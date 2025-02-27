from itertools import permutations
    from string import ascii_letters

def palindromes_between_indices(s):
    s = ''.join((c for c in s.lower() if c in ascii_letters))
    between = s[1:8]
    palindromes = set()
    for p in range(3, len(between) + 1):
        for perm in permutations(between, p):
            if ''.join(perm) == ''.join(reversed(''.join(perm))):
                palindromes.add(''.join(perm))
    return palindromes