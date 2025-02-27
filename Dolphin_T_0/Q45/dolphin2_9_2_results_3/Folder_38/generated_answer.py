from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:9] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters, 5):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word.lower())
    return palindromes