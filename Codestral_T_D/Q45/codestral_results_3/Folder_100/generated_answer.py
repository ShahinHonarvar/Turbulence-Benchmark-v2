import itertools

def palindromes_between_indices(string):
    substring = string[0:6]
    letters = [char.lower() for char in substring if char.isalpha()]
    permutations = itertools.permutations(letters, len(letters))
    palindromes = set()
    for perm in permutations:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes