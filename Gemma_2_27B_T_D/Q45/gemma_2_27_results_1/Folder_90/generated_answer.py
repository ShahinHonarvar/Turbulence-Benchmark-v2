from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[0:6].lower() if c.isalpha()))
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes