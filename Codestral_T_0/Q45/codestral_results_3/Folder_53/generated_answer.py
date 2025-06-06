from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    palindromes = set()
    for p in permutations(s, len(s)):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes