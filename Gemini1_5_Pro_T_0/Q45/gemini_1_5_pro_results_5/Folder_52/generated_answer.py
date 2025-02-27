from itertools import permutations

def palindromes_between_indices(string):
    letters = set([char.lower() for char in string[0:8] if char.isalpha()])
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes