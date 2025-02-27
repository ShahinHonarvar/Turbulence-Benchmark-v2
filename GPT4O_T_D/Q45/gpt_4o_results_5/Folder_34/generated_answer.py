from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substring = s[5:8].lower()
    possible_chars = [c for c in substring if c.isalpha()]
    possible_palindromes = set()
    for length in range(4, len(possible_chars) + 1):
        for perm in permutations(possible_chars, length):
            if perm == perm[::-1]:
                possible_palindromes.add(''.join(perm))
    return possible_palindromes