import itertools

def palindromes_between_indices(string):
    letters = set([string[i].lower() for i in range(5, 8) if string[i].isalpha()])
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes