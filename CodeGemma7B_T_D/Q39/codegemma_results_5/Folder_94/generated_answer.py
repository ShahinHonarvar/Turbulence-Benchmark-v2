from functools import cmp_to_key

def return_n_greatest_chars(str):
    return sorted(str, key=cmp_to_key(lambda x, y: y.encode('utf-8').item(0) - x.encode('utf-8').item(0)), reverse=True)[:87]