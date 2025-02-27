from itertools import permutations

def palindromes_between_indices(string):
    substr = string[2:10]
    substr = substr.lower()
    palindromes_set = set()
    for i in range(4, len(substr) + 1):
        perms = permutations(substr, i)
        for perm in perms:
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes_set.add(word)
    return palindromes_set