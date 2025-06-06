from itertools import permutations

def palindromes_between_indices(string):
    letters = {string[i].lower() for i in range(4) if string[i].isalpha()}
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for p in permutations(letters, length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes