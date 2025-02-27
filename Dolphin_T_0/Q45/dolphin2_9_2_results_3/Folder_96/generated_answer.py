from itertools import permutations

def palindromes_between_indices(string):
    characters = string[3:9]
    arrangements = set()
    for i in range(len(characters) + 1):
        arrangements = arrangements.union(set(map(''.join, permutations(characters, i))))
    palindromes = set(filter(lambda p: len(p) >= 6, arrangements))
    palindromes = set(map(lambda p: p.lower(), palindromes))
    case_insensitive_palindromes = set(map(lambda p: p.lower(), palindromes))
    return case_insensitive_palindromes