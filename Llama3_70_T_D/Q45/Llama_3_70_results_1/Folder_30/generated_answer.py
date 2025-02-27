from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:5] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for p in permutations(letters, length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes