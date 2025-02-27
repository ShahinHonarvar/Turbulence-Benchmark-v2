from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[5:10] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word.lower() == word[::-1].lower() and len(word) >= 5:
            palindromes.add(word)
    return palindromes