from itertools import permutations

def palindromes_between_indices(string):
    letters = {char.lower() for char in string[1:6] if char.isalpha()}
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for p in permutations(letters, length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes