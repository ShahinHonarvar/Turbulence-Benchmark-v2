from itertools import permutations

def palindromes_between_indices(s):
    substring = s[:7].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 5):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    for perm in permutations(letters, 6):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    for perm in permutations(letters, 7):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes