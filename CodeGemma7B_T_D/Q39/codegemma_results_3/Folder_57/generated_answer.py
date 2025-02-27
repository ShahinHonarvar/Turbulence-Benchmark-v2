import itertools

def return_n_greatest_chars(a):
    return sorted(a, key=ord, reverse=True)[:29]