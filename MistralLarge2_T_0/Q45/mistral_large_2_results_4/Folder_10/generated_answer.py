from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[:6] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm).lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes