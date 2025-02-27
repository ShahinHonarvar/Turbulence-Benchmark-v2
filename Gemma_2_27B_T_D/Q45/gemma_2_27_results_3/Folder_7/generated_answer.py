from itertools import permutations

def palindromes_between_indices(text):
    letters = [char for char in text[1:10] if char.isalpha()]
    palindromes = set()
    for permu in permutations(letters):
        word = ''.join(permu).lower()
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes