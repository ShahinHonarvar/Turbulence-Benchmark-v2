from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[1:8] if char.isalpha())).lower()
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for candidate in permutations(letters, length):
            word = ''.join(candidate)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes