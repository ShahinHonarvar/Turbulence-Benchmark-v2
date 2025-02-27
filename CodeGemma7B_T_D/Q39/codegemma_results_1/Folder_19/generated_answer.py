from collections import Counter
from functools import cmp_to_key

def return_n_greatest_chars(char_str):
    return sorted(char_str, key=cmp_to_key(lambda x, y: ord(x) - ord(y)), reverse=False)[:58]