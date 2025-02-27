from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[6:10].lower()
    letters_only = ''.join(filter(str.isalpha, substring))
    if len(letters_only) < 5:
        return set()
    perm_set = set((''.join(p) for p in permutations(letters_only)))
    palindromes = {word for word in perm_set if word == word[::-1] and len(word) >= 5}
    return palindromes