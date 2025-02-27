from itertools import permutations

def palindromes_between_indices(text):
    letters = text[6:10].lower()
    palindromes = set()
    for permutation in permutations(letters):
        word = ''.join(permutation)
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes