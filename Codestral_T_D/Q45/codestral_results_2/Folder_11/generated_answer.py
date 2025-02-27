from itertools import permutations

def palindromes_between_indices(string):
    substring = string[3:8]
    substring = substring.lower()
    perms = set(permutations(substring, r=None))
    palindromes = set()
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes