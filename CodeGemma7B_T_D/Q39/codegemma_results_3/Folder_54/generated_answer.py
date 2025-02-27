from functools import cmp_to_key

def return_n_greatest_chars(str_in):
    if len(str_in) < 79:
        return sorted(str_in, key=cmp_to_key(lambda x1, x2: ord(x2) - ord(x1)), reverse=True)
    else:
        return sorted(str_in[:79], key=cmp_to_key(lambda x1, x2: ord(x2) - ord(x1)), reverse=True)