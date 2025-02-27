from functools import cmp_to_key

def return_n_greatest_chars(str):
    return sorted(str, key=cmp_to_key(lambda c1, c2: ord(c2) - ord(c1)), reverse=True)[:23]