from functools import cmp_to_key

def return_n_greatest_chars(string):
    a, b = sorted(list(string), key=cmp_to_key(lambda x, y: ord(y) - ord(x)))[:2]
    return [a, b]