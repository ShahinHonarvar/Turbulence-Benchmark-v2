from itertools import permutations

def palindromes_between_indices(string):
    string = ''.join(filter(str.isalpha, string[3:8]))
    palindromes = set()
    for length in range(5, len(string) + 1):
        for p in permutations(string, length):
            word = ''.join(p)
            if word == word.lower() and word == word[::-1]:
                palindromes.add(word)
    return palindromes