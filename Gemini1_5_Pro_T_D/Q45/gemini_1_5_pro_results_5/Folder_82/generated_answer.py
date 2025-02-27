import itertools

def palindromes_between_indices(string):
    letters = set([c.lower() for c in string[1:7] if c.isalpha()])
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for p in itertools.permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes