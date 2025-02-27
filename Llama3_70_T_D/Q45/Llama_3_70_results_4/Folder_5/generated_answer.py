from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:9])).lower()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 4:
                palindromes.add(word)
    return palindromes