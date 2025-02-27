import itertools

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[2:5] if c.isalpha())).lower()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for permutation in itertools.permutations(letters, length):
            word = ''.join(permutation)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes