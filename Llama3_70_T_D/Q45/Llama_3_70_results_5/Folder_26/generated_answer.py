from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:7].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        perms = permutations(letters, r)
        for perm in perms:
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes