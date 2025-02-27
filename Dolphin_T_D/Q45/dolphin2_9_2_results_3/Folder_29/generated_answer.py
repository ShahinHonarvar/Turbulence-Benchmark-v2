from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10]
    s = ''.join(filter(str.isalpha, s)).lower()
    if len(set(s)) < 6:
        return set()
    palindromes = set()
    for p in permutations(s, len(s)):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes