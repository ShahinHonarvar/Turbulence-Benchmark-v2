from itertools import permutations

def palindromes_between_indices(s):
    letters = set((s[i].lower() for i in range(8, 10) if s[i].isalpha()))
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes