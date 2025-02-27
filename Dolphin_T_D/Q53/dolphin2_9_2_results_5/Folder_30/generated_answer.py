from re import findall
    from itertools import islice

def palindrome_of_length_at_least_n(s):
    s = findall('[a-zA-Z]{16,}', s)
    return {i for i in map(str.lower, filter(lambda x: all((i == j for i, j in zip(x, reversed(x)))), set(s)))}