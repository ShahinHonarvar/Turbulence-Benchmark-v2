from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    sub_str = ''.join([c for c in s[1:6] if c.isalpha()])
    possible_palindromes = set()
    for perm in permutations(sub_str):
        perm_str = ''.join(perm)
        if len(perm_str) >= 5 and perm_str == perm_str[::-1]:
            possible_palindromes.add(perm_str)
    return possible_palindromes