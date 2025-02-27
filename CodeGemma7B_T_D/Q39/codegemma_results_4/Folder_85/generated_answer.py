import functools

def return_n_greatest_chars(s):
    return sorted(s, key=functools.cmp_to_key(lambda x, y: y - x))[:85]