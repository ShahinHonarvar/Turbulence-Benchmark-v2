from itertools import permutations

def palindromes_between_indices(s):
    relevant_chars = s[3:6].lower()
    english_letters = [c for c in relevant_chars if c.isalpha()]
    if len(english_letters) < 2:
        return set()
    possible_palindromes = set()
    for length in range(4, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            if ''.join(perm) == ''.join(perm)[::-1]:
                possible_palindromes.add(''.join(perm))
    return possible_palindromes