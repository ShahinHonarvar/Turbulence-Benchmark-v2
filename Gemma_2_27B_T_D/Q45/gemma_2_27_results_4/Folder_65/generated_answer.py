from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[0:7] if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 5):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes