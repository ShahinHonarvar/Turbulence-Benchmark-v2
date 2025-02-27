from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:8].lower()
    palindromes = set()
    for p in permutations(s):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes