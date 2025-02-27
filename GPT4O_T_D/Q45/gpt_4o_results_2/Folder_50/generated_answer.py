from itertools import permutations

def palindromes_between_indices(s):
    segment = s[4:9].lower()
    letters = [c for c in segment if c.isalpha()]
    palindromes = set()
    if len(letters) < 5:
        return palindromes
    for perm in set(permutations(letters, len(letters))):
        word = ''.join(perm)
        if len(word) >= 5 and word == word[::-1]:
            palindromes.add(word)
    return palindromes