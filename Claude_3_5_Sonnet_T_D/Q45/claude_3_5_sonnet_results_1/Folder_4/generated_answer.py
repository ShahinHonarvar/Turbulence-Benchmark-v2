from itertools import permutations

def palindromes_between_indices(input_string):
    subset = ''.join((char.lower() for char in input_string[3:10] if char.isalpha()))
    palindromes = set()
    for length in range(7, len(subset) + 1):
        for perm in permutations(subset, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes