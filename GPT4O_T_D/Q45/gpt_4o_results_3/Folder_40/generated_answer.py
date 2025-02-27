from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    valid_chars = ''.join(filter(str.isalpha, substring))
    if len(valid_chars) < 7:
        return set()
    perms = set(permutations(valid_chars))
    palindromes = set()
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return {p for p in palindromes if len(p) >= 7}