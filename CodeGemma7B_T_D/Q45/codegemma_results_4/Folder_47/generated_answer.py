from itertools import permutations

def palindromes_between_indices(text):
    text = text[3:7].lower()
    words = [''.join(p) for p in permutations(text)]
    palindromes = {word for word in words if word == word[::-1] and len(word) >= 5}
    return palindromes