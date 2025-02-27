import itertools

def palindromes_between_indices(string):
    letters = set()
    for i in range(1, 8):
        if string[i].isalpha():
            letters.add(string[i].lower())
    palindromes = set()
    for i in range(7, len(string) + 1):
        for permutation in itertools.permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes