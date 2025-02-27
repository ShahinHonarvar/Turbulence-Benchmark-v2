from itertools import permutations

def palindromes_between_indices(text):
    substring = text[3:9]
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 7 and word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes