from itertools import permutations

def palindromes_between_indices(string):
    characters = string[7:10].lower()
    palindromes = set()
    for permutation in permutations(characters):
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes