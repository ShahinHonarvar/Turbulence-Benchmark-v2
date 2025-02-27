from itertools import permutations

def palindromes_between_indices(text):
    letters = [c.lower() for c in text[2:9] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes