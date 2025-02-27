from itertools import permutations

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[1:5] if char.isalpha()]
    perms = set(permutations(letters, r=None))
    palindromes = set()
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes