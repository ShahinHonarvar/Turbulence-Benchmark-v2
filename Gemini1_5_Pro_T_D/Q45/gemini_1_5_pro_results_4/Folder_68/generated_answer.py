import itertools

def palindromes_between_indices(string):
    letters = set([c.lower() for c in string[1:9] if c.isalpha()])
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes