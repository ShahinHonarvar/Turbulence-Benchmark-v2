from functools import cmp_to_key

def return_n_greatest_chars(str_in):
    str_in = sorted(str_in, key=cmp_to_key(lambda x, y: ord(y) - ord(x)))
    return str_in[:47]