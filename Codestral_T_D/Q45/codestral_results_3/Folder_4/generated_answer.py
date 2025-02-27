from itertools import permutations

def palindromes_between_indices(string):
    substring = string[3:10].lower()
    palindromes = set()
    for i in range(7, len(substring) + 1):
        for perm in permutations(substring, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes