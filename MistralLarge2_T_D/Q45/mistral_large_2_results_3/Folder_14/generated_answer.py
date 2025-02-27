import re
    from itertools import permutations

def palindromes_between_indices(s):
    substr = re.findall('[a-zA-Z]', s[4:6])
    substr = ''.join(substr).lower()
    palindromes = set()
    for length in range(3, len(substr) + 1):
        for perm in permutations(substr, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes