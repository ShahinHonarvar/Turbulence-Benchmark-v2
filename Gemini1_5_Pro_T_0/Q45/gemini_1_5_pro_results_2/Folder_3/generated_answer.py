import itertools

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[7:10] if c.isalpha())).lower()
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes