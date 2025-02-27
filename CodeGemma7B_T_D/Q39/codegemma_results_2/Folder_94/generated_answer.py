from functools import cmp_to_key

def return_n_greatest_chars(string):
    chars = list(string)
    chars.sort(key=cmp_to_key(lambda a, b: ord(b) - ord(a)))
    return chars[:87]