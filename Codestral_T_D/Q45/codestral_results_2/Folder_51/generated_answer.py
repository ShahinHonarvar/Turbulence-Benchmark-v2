from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:6].lower()
    palindromes = set()
    for l in range(3, len(s) + 1):
        for p in permutations(s, l):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes