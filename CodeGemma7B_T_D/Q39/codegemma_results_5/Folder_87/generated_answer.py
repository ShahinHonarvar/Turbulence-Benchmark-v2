from functools import cmp_to_key

def return_n_greatest_chars(lst):
    return sorted(lst, key=cmp_to_key(lambda x, y: ord(y) - ord(x)), reverse=False)[:24]