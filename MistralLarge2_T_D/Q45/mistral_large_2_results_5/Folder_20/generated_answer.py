import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:9] if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in itertools.permutations(letters, length):
            perm_str = ''.join(perm).lower()
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes