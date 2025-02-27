from itertools import permutations

def palindromes_between_indices(s):
    letters = [ch for ch in s[4:7] if ch.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for p in permutations(letters, len(letters)):
        word = ''.join(p).lower()
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes