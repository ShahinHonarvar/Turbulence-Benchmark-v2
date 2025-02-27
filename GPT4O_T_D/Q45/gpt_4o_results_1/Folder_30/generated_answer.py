from itertools import permutations

def palindromes_between_indices(s):
    English_letters = ''.join([c.lower() for c in s[:5] if c.isalpha()])
    potential_palindromes = set()
    for length in range(4, len(English_letters) + 1):
        for perm in permutations(English_letters, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                potential_palindromes.add(perm_str)
    return potential_palindromes