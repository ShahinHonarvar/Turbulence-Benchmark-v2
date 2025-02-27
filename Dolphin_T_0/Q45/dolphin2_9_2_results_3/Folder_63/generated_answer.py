from itertools import permutations

def palindromes_between_indices(s):
    l = s[:4].lower()
    palindromes = set()
    for p in permutations(l, 3, repetition=''):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes