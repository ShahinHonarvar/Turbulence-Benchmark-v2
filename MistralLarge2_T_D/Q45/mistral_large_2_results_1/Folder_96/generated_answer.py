from itertools import permutations

def palindromes_between_indices(s):
    chars = [c for c in s[3:9] if c.isalpha()]
    chars = [c.lower() for c in chars]
    palindromes = set()
    for length in range(6, len(chars) + 1):
        for perm in permutations(chars, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes