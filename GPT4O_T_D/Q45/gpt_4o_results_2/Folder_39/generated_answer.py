from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    segment = ''.join([char for char in s[2:6] if char.isalpha()])
    palindromes = set()
    for perm in permutations(segment):
        perm_str = ''.join(perm)
        if len(perm_str) >= 3 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes