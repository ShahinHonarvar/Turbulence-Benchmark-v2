from itertools import permutations

def palindromes_between_indices(text):
    letters = text[2:4]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word.lower() == word[::-1].lower() and len(word) >= 3:
            palindromes.add(word)
    return palindromes