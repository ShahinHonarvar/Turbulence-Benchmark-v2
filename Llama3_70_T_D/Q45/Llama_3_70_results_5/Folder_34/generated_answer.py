from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:8].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes