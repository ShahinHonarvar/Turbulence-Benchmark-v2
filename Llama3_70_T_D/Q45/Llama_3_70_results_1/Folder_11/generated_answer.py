from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:8].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes