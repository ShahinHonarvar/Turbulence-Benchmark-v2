from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    letters = [c for c in substring if c.isalpha()]
    if len(letters) < 3:
        return set()
    possible_palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                possible_palindromes.add(word)
    return possible_palindromes