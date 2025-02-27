from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for p in permutations(letters, 5):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes