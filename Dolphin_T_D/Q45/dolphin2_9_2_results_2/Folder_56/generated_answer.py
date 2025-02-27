from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[5:10] if c.isalpha()])
    palindromes = set()
    for p in permutations(letters, len(letters)):
        word = ''.join(p).lower()
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes