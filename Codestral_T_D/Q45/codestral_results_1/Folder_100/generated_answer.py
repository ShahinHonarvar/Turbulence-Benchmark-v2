from itertools import permutations

def palindromes_between_indices(string):
    letters = set(string[0:6].lower())
    palindromes = set()
    for perm in permutations(letters, 6):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes