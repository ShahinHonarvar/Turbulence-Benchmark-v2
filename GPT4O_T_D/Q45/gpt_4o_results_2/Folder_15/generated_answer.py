from itertools import permutations

def palindromes_between_indices(s):
    sub_str = ''.join([c.lower() for c in s[1:3] if c.isalpha()])
    possible_palindromes = set()
    for r in range(3, len(sub_str) + 1):
        for perm in permutations(sub_str, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                possible_palindromes.add(perm_str)
    return possible_palindromes