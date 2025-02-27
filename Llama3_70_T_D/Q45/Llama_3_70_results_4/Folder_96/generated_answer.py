from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = ''.join(filter(str.isalpha, s[3:9]))
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes