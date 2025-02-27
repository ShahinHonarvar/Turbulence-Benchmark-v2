from itertools import permutations

def palindromes_between_indices(text):
    letters = text[5:8]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word.lower() == word.lower()[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes