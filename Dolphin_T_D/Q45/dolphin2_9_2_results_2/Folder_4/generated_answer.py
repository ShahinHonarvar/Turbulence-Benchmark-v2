from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:10] if c.isalpha() and c.isascii()]
    palindromes = set()
    for length in range(7, 10):
        for p in permutations(letters, length):
            word = ''.join(p).lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes