from itertools import permutations

def palindromes_between_indices(string):
    substring = string[2:9].lower()
    perms = set(permutations(substring, r=len(substring)))
    palindromes = set()
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes