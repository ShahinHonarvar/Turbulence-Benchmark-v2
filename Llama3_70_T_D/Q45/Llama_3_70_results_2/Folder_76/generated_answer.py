from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:5].lower()
    palindromes = set()
    for r in range(4, len(s) + 1):
        for perm in permutations(s, r):
            word = ''.join(perm)
            if word == word[::-1] and len(word) >= 4:
                palindromes.add(word)
    return palindromes