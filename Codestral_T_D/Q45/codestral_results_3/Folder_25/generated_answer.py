from itertools import permutations

def palindromes_between_indices(string):
    string = string[1:5].lower()
    palindromes = set()
    for i in range(3, len(string) + 1):
        for p in permutations(string, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes