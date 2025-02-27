from functools import cmp_to_key
from itertools import islice

def return_n_greatest_chars(chars, limit=52):
    return sorted(chars, key=cmp_to_key(lambda x, y: ord(y) - ord(x)))[:limit]