from itertools import product
from string import ascii_lowercase

def palindromes_of_specific_lengths(s):
    hard_coded_range = (63, 70)
    target_length_range = (4, 5)
    result = set()
    for i in range(hard_coded_range[0], hard_coded_range[1] + 1):
        for j in range(i + target_length_range[0], i + target_length_range[1] + 1):
            substring = s[i:j + 1]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                result.add(substring)
    return result