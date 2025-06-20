from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:7].lower()
    palindromes = set()
    for r in range(4, len(s) + 1):
        for perm in permutations(s, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes