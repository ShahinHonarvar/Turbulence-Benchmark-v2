from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    sub_string = string[3:8]
    arrangements = [''.join(p) for p in permutations(sub_string)]
    palindromes = [a for a in arrangements if a == a[::-1] and len(a) >= 6]
    return set(palindromes)