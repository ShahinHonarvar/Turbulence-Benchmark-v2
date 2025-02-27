from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(text[2:6]).lower()
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes