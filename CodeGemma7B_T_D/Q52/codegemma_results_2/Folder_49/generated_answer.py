from itertools import product

def palindrome_of_length_n(string):
    return {s[0]: s[::-1] in string for s in product(string.lower(), repeat=47)}.get(s[0], set())