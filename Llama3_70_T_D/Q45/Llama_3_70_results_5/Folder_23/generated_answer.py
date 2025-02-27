from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(4, len(s) + 1):
        for p in permutations(s, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes