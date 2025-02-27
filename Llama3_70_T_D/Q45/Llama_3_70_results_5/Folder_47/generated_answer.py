from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:8] if char.isalpha()]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes