from itertools import permutations

def palindromes_between_indices(string):
    string = string[2:8].lower()
    palindromes = set()
    for i in range(3, len(string) + 1):
        perms = permutations(string, i)
        for perm in perms:
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes