import itertools

def palindromes_between_indices(string):
    letters = set([char.lower() for char in string[3:10] if char.isalpha()])
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes