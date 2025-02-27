from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    substring = string[5:8]
    perms = permutations(substring)
    palindromes = set()
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes