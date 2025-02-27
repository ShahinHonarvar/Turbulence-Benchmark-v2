from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(text[3:9]).lower()
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if len(word) >= 5 and word == word[::-1]:
            palindromes.add(word)
    return palindromes