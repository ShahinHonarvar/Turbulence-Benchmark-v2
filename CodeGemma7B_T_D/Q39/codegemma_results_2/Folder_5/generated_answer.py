from functools import cmp_to_key
from functools import partial

def return_n_greatest_chars(chars_str):
    ascii_to_char = str.maketrans({i: c for i, c in enumerate(chars_str)})
    return sorted(chars_str, key=partial(cmp_to_key(lambda x, y: y - x), key=ord), reverse=True)[:46]