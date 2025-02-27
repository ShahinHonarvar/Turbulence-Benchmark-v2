from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    sub_str = s[8:10].lower()
    letter_candidates = [char for char in sub_str if char.isalpha()]
    if len(letter_candidates) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(letter_candidates) + 1):
        for perm in permutations(letter_candidates, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes