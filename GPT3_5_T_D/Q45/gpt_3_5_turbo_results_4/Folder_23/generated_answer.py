from itertools import permutations

def palindromes_between_indices(string):
    english_letters = [char for char in string.lower() if char.isalpha()]
    english_letters = english_letters[:7]
    palindromes = set()
    for perm in permutations(english_letters, len(english_letters)):
        perm = ''.join(perm)
        if len(perm) >= 4 and perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes