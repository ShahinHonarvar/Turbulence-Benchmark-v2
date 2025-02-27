import itertools

def palindromes_between_indices(s):
    subset = s[2:6].lower()
    palindromes = set()
    for i in range(5, 0, -1):
        for p in itertools.permutations(subset, i):
            if ''.join(p) == ''.join(reversed(p)):
                palindromes.add(''.join(p))
    return palindromes