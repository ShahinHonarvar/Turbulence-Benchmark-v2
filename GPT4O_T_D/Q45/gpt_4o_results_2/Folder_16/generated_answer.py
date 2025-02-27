from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:10] if c.isalpha()]
    if len(letters) == 0:
        return set()
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for p in permutations(letters, length):
            perm_str = ''.join(p)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes