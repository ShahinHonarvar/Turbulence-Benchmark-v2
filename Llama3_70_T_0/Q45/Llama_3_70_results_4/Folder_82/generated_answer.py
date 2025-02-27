from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if len(word) >= 7 and word == word[::-1]:
            palindromes.add(word)
    return palindromes