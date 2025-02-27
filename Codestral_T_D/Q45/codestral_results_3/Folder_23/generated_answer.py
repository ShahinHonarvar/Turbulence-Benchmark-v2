from itertools import permutations

def palindromes_between_indices(string):
    string = string[0:7].lower()
    length = len(string)
    palindromes = set()
    for i in range(4, length + 1):
        for perm in permutations(string, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes