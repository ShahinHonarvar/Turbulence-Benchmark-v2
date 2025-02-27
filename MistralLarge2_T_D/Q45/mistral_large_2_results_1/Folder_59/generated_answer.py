from itertools import permutations

def palindromes_between_indices(s):
    chars = [ch for ch in s[8:10] if ch.isalpha()]
    chars = ''.join(chars).lower()
    palindromes = set()
    for r in range(3, len(chars) + 1):
        for perm in permutations(chars, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes