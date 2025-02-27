import itertools

def palindromes_between_indices(string):
    letters = string[5:10]
    permutations = itertools.permutations(letters)
    palindromes = set()
    for permutation in permutations:
        word = ''.join(permutation).lower()
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes