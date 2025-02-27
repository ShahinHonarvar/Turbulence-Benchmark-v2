from itertools import permutations

def palindromes_between_indices(string):
    letters = string[6:10]
    palindromes = set()
    for p in permutations(letters, len(letters)):
        word = ''.join(p).lower()
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes