from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([c for c in text[4:8] if c.isalpha()]).lower()
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if len(word) >= 5 and word == word[::-1]:
            palindromes.add(word)
    return palindromes