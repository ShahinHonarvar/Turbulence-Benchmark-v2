from itertools import permutations

def palindromes_between_indices(s):
    palindromes = set()
    for p in permutations(s[6:10], len(s[6:10])):
        word = ''.join(p).lower()
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes