from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((ch for ch in text[1:8] if ch.isalpha())).lower()
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes