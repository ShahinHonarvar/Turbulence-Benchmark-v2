from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[1:8] if c.isalpha()])
    if len(letters) < 7:
        return set()
    palindromes = set()
    for p in permutations(letters, 7):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes