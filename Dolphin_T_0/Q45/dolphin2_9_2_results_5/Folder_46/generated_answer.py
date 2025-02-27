import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10]]
    palindromes = set()
    for r in range(6, 11):
        for t in itertools.combinations(letters, r):
            if ''.join(t).lower() == ''.join(reversed(''.join(t).lower())):
                palindromes.add(''.join(t))
    return palindromes