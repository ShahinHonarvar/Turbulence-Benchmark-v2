from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[2:7] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word.lower() == word.lower()[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes