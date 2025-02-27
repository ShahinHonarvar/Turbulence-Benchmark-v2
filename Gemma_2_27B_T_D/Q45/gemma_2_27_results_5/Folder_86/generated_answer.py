from itertools import permutations

def palindromes_between_indices(string):
    letters = [c for c in string[6:10] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes