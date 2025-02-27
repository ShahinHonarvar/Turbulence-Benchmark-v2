import itertools

def palindromes_between_indices(s):
    substring = ''.join((c for c in s[6:10] if c.isalpha())).lower()
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in itertools.permutations(substring, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes