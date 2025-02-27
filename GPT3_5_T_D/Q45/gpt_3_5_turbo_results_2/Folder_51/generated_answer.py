import itertools
    from itertools import permutations

def palindromes_between_indices(string):
    letters = [letter for letter in string[3:6] if letter.isalpha()]
    permutations = set(itertools.permutations(letters, len(letters)))
    palindromes = set()
    for perm in permutations:
        word = ''.join(perm)
        if word.lower() == word.lower()[::-1] and len(word) >= 3:
            palindromes.add(word.lower())
    return palindromes