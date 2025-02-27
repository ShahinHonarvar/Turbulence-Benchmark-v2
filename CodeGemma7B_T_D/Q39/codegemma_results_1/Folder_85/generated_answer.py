from functools import cmp_to_key

def return_n_greatest_chars(a):
    a = sorted(a, key=cmp_to_key(lambda x, y: y.lower().encode()[-1] - x.lower().encode()[-1]), reverse=True)
    return a[:85]