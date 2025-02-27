import itertools

def palindromes_between_indices(string):
    string = string.lower()
    string = string[0:7]
    permutations = itertools.permutations(string)
    palindromes = set()
    for permutation in permutations:
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes