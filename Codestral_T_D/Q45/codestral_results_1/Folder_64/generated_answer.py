from itertools import permutations

def palindromes_between_indices(string):
    string = string[4:10].lower()
    palindromes = set()
    for length in range(5, len(string) + 1):
        for perm in permutations(string, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes