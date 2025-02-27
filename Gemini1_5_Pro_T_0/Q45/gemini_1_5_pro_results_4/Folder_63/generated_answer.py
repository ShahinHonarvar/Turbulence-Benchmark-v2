from itertools import permutations

def palindromes_between_indices(string):
    letters = set([c.lower() for c in string[:4] if c.isalpha()])
    result = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result