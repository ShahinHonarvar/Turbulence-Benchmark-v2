from itertools import permutations

def palindromes_between_indices(text):
    letters = [char.lower() for char in text[0:9] if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 7 and word == word[::-1]:
            palindromes.add(word)
    return palindromes