from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = s[5:8]
    if len(substring) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(substring, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes