from itertools import permutations

def palindromes_between_indices(text):
    letters = [char for char in text[3:10] if char.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word.lower() == word.lower()[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes