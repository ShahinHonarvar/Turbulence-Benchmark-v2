from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[4:7] if char.isalpha())).lower()
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for permutation in permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes