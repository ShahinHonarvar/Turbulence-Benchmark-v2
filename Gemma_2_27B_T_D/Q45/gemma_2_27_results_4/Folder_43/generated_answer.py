from itertools import permutations

def palindromes_between_indices(text):
    letters = text[2:6].lower()
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes