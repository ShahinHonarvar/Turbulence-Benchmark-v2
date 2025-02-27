from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:10].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(7, len(s) + 1):
        for p in permutations(s, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes