from itertools import permutations

def palindromes_between_indices(text):
    letters = text[3:9].lower()
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes