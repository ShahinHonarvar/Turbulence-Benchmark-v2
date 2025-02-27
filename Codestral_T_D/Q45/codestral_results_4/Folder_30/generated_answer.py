import itertools

def palindromes_between_indices(string):
    string = string.lower()
    letters = string[0:5]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for permutation in itertools.permutations(letters, length):
            word = ''.join(permutation)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes