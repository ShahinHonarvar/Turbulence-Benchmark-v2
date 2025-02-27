from itertools import permutations

def palindromes_between_indices(s):
    letters = s[2:6]
    palindromes = set()
    for p in range(4, len(letters) + 1):
        for perm in permutations(letters, p):
            word = ''.join(perm)
            if word == word.lower() and word == word[::-1]:
                palindromes.add(word)
    return palindromes