from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:10]
    palindromes = set()
    for p in permutations(s.lower(), 4):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes