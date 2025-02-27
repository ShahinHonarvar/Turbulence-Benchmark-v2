from itertools import permutations

def palindromes_between_indices(string):
    string = string[0:3].lower()
    palindromes = set()
    for p in permutations(string):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes