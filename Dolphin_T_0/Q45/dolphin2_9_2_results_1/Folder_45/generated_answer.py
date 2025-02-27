from itertools import permutations

def palindromes_between_indices(input_string):
    substring = input_string[5:10]
    possibilities = list(map(''.join, permutations(substring)))
    palindromes = set(filter(lambda x: len(x) >= 4 and x.lower() == x.lower()[::-1], possibilities))
    return palindromes