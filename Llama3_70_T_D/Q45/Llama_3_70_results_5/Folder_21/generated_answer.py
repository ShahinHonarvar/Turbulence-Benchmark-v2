from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:9] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters, 7):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes