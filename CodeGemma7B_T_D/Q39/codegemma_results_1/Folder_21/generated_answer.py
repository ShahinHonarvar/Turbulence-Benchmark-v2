from functools import cmp_to_key

def return_n_greatest_chars(str):
    return sorted(str, key=cmp_to_key(lambda a, b: -ord(a) + ord(b)))[:44]