import itertools

def palindromes_between_indices(string):
    letters = set([c.lower() for c in string[1:5] if c.isalpha()])
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes