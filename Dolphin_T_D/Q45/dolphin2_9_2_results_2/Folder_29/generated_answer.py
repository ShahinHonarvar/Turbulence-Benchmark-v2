from itertools import permutations

def palindromes_between_indices(s):
    palindromes = set()
    for p in permutations(s[2:10], len(s[2:10])):
        word = ''.join(p).lower()
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes