from itertools import permutations

def palindromes_between_indices(input_string):
    input_string = input_string[2:5]
    palindrome_versions = [''.join(p) for p in permutations(input_string)]
    palindromes = set(filter(lambda x: len(x) >= 4 and x == x[::-1], palindrome_versions))
    return palindromes