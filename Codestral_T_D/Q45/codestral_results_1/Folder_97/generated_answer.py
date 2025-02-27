from itertools import permutations

def palindromes_between_indices(string):
    palindromes = set()
    string = string.lower()
    substring = string[0:5]
    perms = permutations(substring)
    for perm in perms:
        word = ''.join(perm)
        if len(word) >= 3 and word == word[::-1]:
            palindromes.add(word)
    return palindromes