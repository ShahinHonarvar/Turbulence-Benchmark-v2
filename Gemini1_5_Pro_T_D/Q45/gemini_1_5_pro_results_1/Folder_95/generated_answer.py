from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[7:9] if char.isalpha())).lower()
    result = set()
    for i in range(3, len(letters) + 1):
        for permutation in permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                result.add(word)
    return result