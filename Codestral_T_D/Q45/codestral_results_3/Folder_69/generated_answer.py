from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [char for char in s[0:4] if char.isalpha()]
    perms = permutations(letters)
    palindromes = set()
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes