from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    length = min(7, len(string))
    palindromes = set()
    for r in range(6, length + 1):
        for perm in permutations(string[:7], r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes