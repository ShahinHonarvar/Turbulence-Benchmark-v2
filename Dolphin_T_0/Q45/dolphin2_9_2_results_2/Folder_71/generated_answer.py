from itertools import permutations

def palindromes_between_indices(s):
    palindromes = set()
    for p in permutations(s[1:4], len(s[1:4])):
        word = ''.join(p).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes