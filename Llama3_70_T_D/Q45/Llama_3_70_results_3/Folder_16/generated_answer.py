from itertools import permutations

def palindromes_between_indices(s):
    letters = set(s[6:10].lower())
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes