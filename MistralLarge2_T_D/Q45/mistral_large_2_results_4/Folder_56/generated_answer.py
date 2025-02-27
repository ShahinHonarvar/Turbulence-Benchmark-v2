from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    chars = ''.join((c for c in s[5:10] if c.isalpha())).lower()
    char_count = Counter(chars)
    palindromes = set()
    for length in range(5, len(chars) + 1):
        for perm in permutations(chars, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes