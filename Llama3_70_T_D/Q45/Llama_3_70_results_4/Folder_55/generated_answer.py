from itertools import permutations

def palindromes_between_indices(s):
    s = s[:3].lower()
    length = len(s)
    palindromes = set()
    for r in range(3, length + 1):
        for p in permutations(s, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes