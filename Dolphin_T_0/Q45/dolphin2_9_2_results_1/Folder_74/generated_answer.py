from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7]
    palindromes = set()
    for p in permutations(s, len(s)):
        word = ''.join(p).lower()
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes