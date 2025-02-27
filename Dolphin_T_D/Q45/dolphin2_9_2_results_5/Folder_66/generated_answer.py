from itertools import permutations
    import re

def palindromes_between_indices(s):
    s = re.sub('[^A-Za-z]', '', s[:6])
    s = ''.join(sorted(s.lower()))
    palindromes = set()
    for p in range(5, 0, -1):
        for perm in permutations(s, p):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes