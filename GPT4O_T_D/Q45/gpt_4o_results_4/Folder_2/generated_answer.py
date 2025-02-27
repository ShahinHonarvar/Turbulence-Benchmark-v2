from itertools import permutations

def palindromes_between_indices(s):
    s_mid = s[1:6].lower()
    letters_only = [c for c in s_mid if c.isalpha()]
    if len(letters_only) < 6:
        return set()
    palindromes = set()
    for perm in permutations(letters_only, 6):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes