from itertools import permutations

def palindromes_between_indices(s):
    set_of_palindromes = set()
    for i in permutations(s[4:9]):
        if i == i[::-1]:
            set_of_palindromes.add(''.join(i).lower())
    return set_of_palindromes