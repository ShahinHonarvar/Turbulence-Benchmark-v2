from itertools import permutations

def palindromes_between_indices(text):
    letters = text[4:9].replace(' ', '').lower()
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes