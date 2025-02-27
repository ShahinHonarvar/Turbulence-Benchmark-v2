import itertools

def palindromes_between_indices(string):
    letters = set([c.lower() for c in string[6:9] if c.isalpha()])
    palindromes = set()
    for l in range(4, len(letters) + 1):
        for p in itertools.permutations(letters, l):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes