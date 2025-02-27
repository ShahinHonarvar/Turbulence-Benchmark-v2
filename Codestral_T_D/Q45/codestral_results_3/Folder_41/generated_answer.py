from itertools import permutations

def palindromes_between_indices(s):
    letters = s[2:4].lower()
    palindromes = set()
    for p in permutations(letters, len(letters)):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes