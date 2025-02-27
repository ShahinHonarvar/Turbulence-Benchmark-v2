from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[4:7] if char.isalpha())).lower()
    palindromes = set()
    if len(letters) >= 3:
        for length in range(3, len(letters) + 1):
            for permutation in permutations(letters, length):
                word = ''.join(permutation)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes