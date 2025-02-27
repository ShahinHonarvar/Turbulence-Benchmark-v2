import itertools

def palindromes_between_indices(s):
    substring = ''.join(sorted([ch.lower() for ch in s[2:7]]))
    palindromes = set()
    for i in range(4, len(substring) + 1):
        for p in itertools.permutations(substring, i):
            if ''.join(p) == ''.join(reversed(p)):
                palindromes.add(''.join(p))
    return palindromes