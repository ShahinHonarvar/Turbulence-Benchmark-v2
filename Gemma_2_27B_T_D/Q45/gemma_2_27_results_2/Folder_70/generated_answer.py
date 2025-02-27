from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([char.lower() for char in text[1:7] if char.isalpha()])
    palindromes = set()
    for permutation in permutations(letters):
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes