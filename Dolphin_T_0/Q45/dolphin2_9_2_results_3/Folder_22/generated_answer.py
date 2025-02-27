from itertools import permutations

def palindromes_between_indices(s):
    perm = permutations(s[5:7], 3)
    palindromes = set()
    for p in list(perm):
        word = ''.join(p)
        if word.lower() == word.lower()[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes