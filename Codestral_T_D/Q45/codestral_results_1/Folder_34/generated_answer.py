from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    substring = string[5:8]
    palindromes = set()
    for r in range(4, len(substring) + 1):
        for perm in permutations(substring, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes