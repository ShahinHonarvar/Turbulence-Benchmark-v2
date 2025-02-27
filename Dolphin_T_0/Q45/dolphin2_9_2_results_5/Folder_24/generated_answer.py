from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:10] if c.isalpha()]
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p).lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes