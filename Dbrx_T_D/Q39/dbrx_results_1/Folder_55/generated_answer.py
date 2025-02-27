import collections

def return_n_greatest_chars(s):
    s = sorted(s, key=collections.Counter(s).get, reverse=True)
    return s[:75]