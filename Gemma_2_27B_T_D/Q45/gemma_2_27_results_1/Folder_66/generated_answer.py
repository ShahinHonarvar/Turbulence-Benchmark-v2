from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[0:6])).lower()
    palindromes = set()
    for p in permutations(letters, 5):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes