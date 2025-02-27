import itertools

def palindromes_between_indices(text):
    letters = set([c.lower() for c in text[5:8] if c.isalpha()])
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for p in itertools.permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes