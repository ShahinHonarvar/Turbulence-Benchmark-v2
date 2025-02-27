from functools import cmp_to_key

def return_n_greatest_chars(string):
    list = sorted(string, key=cmp_to_key(lambda x, y: ord(y) - ord(x)), reverse=False)[:5]
    return list