from itertools import permutations

def palindromes_between_indices(s):
    letters = s[5:8].lower()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes