import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[3:7] if c.isalpha()]
    letters = [c.lower() for c in letters]
    unique_letters = set(letters)
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in itertools.permutations(unique_letters, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes