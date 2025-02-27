from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((char for char in s[:7] if char.isalpha())).lower()
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes