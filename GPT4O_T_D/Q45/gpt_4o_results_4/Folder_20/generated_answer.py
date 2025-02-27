from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = ''.join(filter(str.isalpha, s[2:9]))
    result = set()
    unique_permutations = set(permutations(substring))
    for perm in unique_permutations:
        perm_str = ''.join(perm)
        for length in range(4, len(perm_str) + 1):
            word = perm_str[:length]
            if word == word[::-1]:
                result.add(word)
    return result