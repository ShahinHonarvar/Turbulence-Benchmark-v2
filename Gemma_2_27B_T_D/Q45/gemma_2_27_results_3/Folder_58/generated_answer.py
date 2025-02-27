from itertools import permutations

def palindromes_between_indices(text):
    letters = [letter for letter in text[:7] if letter.isalpha()]
    palindromes = set()
    for permutation in permutations(letters):
        word = ''.join(permutation)
        if word.lower() == word.lower()[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes