import re
    from itertools import permutations

def palindromes_between_indices(s):
    substring = re.sub('[^a-zA-Z]', '', s[2:10]).lower()
    unique_chars = set(substring)
    all_permutations = set((''.join(p) for l in range(4, len(substring) + 1) for p in permutations(substring, l)))
    palindromes = set((p for p in all_permutations if p == p[::-1]))
    return palindromes