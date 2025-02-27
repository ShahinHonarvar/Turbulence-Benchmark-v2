from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = ''.join(filter(str.isalpha, s[1:4]))
    palindromes = set()
    for r in range(4, len(s) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes