from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted([char.lower() for char in string[1:7] if char.isalpha()]))
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes