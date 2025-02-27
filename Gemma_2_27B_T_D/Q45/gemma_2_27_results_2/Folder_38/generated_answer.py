from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([c for c in text[3:9] if c.isalpha()])
    letter_set = set(letters)
    palindromes = set()
    for perm in permutations(letter_set, 5):
        word = ''.join(perm)
        if word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    return palindromes