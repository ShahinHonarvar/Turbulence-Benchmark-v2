from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:9] if c.isalpha())).lower()
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 6 and word == word[::-1]:
            palindromes.add(word)
    return palindromes