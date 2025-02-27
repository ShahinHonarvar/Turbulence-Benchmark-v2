from itertools import permutations

def palindromes_between_indices(string):
    letters = [char for char in string[2:10] if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes