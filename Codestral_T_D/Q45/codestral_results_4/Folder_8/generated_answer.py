from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    length = len(s)
    palindromes = set()
    for i in range(5, length + 1):
        for p in permutations(s, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes