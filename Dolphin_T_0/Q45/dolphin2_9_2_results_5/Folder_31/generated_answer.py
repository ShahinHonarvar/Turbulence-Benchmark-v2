import string
from itertools import permutations

def palindromes_between_indices(s):
    palindromes = set()
    for i in range(1, 9):
        for j in range(i + 2, len(s) + 1):
            substr = s[i:j]
            if len(substr) >= 6:
                list_substr = list(substr.lower())
                for p in permutations(list_substr):
                    pal_str = ''.join(p)
                    if pal_str == pal_str[::-1]:
                        palindromes.add(pal_str)
    return palindromes