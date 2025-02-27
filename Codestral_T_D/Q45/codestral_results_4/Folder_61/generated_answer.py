from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    substring = string[0:8]
    palindromes = set()
    for i in range(7, len(substring) + 1):
        for p in permutations(substring, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes