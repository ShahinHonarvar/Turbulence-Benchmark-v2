from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        word = ''.join(perm)
        if len(word) >= 7 and word == word[::-1]:
            palindromes.add(word)
    return palindromes