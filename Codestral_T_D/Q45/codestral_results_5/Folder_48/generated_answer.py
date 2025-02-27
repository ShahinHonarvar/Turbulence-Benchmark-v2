from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:9].lower()
    palindromes = set()
    for p in permutations(s, len(s)):
        word = ''.join(p)
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes