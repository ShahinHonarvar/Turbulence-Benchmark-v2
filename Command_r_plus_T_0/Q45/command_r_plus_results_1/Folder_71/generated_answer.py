from itertools import permutations

def palindromes_between_indices(s):
    letters = [char for char in s[1:4] if char.isalpha()]
    letters = [char.lower() for char in letters]
    all_permutations = permutations(letters)
    palindromes = set()
    for perm in all_permutations:
        word = ''.join(perm)
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes