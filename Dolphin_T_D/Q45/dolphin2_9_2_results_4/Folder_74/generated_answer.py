from itertools import permutations

def palindromes_between_indices(string):
    substring = string[1:7].lower()
    permutations = [''.join(p) for i in range(6, len(substring) + 1) for p in permutations(substring, i)]
    palindromes = set(filter(lambda p: p == p[::-1], permutations))
    return palindromes