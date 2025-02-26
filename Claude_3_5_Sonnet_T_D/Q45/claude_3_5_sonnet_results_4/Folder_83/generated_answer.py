from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:10] if c.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes