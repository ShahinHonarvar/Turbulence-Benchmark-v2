from itertools import permutations

def palindromes_between_indices(text):
    letters = text[2:10]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word.lower() == word.lower()[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes