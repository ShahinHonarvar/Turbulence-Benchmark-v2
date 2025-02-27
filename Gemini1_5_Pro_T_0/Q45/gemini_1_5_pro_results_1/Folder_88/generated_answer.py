from itertools import permutations

def palindromes_between_indices(text):
    letters = set([c for c in text[3:8].lower() if c.isalpha()])
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes