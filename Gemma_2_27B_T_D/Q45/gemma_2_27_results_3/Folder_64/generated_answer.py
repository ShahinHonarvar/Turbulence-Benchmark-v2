from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join([c for c in text[4:10] if c.isalpha()]).lower()
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes