from functools import cmp_to_key

def return_n_greatest_chars(str):
    str_list = list(str)
    str_list.sort(key=cmp_to_key(lambda x, y: ord(y) - ord(x)))
    return str_list[:80]