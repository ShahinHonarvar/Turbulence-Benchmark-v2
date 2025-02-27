from itertools import permutations

def palindromes_between_indices(s):
    palindromes = set()
    for p in permutations(s[0:6].lower(), r=6):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes