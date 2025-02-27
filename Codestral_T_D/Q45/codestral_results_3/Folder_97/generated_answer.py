from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    substring = string[0:5]
    palindromes = set()
    for perm in permutations(substring, 3):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes