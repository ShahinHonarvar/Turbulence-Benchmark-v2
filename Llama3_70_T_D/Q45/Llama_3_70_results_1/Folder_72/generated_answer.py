from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters, 6):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes