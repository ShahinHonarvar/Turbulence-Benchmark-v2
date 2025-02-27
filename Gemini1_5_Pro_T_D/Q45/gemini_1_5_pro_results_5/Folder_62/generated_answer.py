from itertools import permutations

def palindromes_between_indices(string):
    letters = set([c for c in string[:9] if c.isalpha()])
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word.lower() == word[::-1].lower():
                palindromes.add(word.lower())
    return palindromes