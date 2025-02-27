from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = ''.join([char for i, char in enumerate(s[:7]) if char.isalpha()])
    result = set()
    for length in range(4, len(substring) + 1):
        for perm in permutations(substring, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                result.add(perm_str)
    return result