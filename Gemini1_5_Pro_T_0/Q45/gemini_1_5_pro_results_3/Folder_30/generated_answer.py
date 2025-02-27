from itertools import permutations

def palindromes_between_indices(string):
    letters = set([c.lower() for c in string[:5] if c.isalpha()])
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes