from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    substring = s[3:7].lower()
    letters = [c for c in substring if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 3 and word == word[::-1]:
            palindromes.add(word)
    return palindromes