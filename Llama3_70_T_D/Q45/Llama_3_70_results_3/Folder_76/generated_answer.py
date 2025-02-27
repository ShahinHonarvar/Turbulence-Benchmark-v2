from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:5].lower() if c.isalpha()]
    palindromes = set()
    for p in permutations(letters, 4):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes