import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[3:5] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes