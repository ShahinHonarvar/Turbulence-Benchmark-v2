from itertools import permutations

def palindromes_between_indices(input_string):
    palindromes = set()
    for p in permutations(input_string[2:9], 4):
        if ''.join(p).lower() == ''.join(reversed(p)).lower():
            palindromes.add(''.join(p))
    return palindromes