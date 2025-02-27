from functools import cmp_to_key

def return_n_greatest_chars(string):
    funcs = (len, ord)
    chars = sorted(string, key=cmp_to_key(funcs))
    return chars[-10:]