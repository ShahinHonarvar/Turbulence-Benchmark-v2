from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted([c.lower() for c in s[1:3]]))
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes