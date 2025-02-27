from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    chars = [c for c in s[5:8] if c.isalpha()]
    palindromes = set()
    for r in range(4, len(chars) + 1):
        for perm in permutations(chars, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes