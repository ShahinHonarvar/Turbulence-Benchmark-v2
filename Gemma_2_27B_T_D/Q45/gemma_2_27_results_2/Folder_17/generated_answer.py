from itertools import permutations

def palindromes_between_indices(s):
    letters = [char for char in s[2:7] if char.isalpha()]
    palindromes = set()
    for permutation in permutations(letters):
        word = ''.join(permutation).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes