from itertools import permutations

def palindromes_between_indices(string):
    string = string[1:10].lower()
    palindromes = set()
    for length in range(7, len(string) + 1):
        for p in permutations(string, length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes