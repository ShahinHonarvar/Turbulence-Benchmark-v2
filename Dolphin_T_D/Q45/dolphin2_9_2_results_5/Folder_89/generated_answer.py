from itertools import permutations

def palindromes_between_indices(string):
    string = string[5:10]
    palindromes = set()
    for p in range(6, len(string) + 1):
        for perm in permutations(string, p):
            word = ''.join(perm)
            if word == word.lower() and word == word[::-1]:
                palindromes.add(word)
    return palindromes