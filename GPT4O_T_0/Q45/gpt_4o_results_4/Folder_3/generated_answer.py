from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[7:10].lower()
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(substring, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes