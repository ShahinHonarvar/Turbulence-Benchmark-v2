from functools import cmp_to_key

def return_n_greatest_chars(chars):
    return sorted(chars, key=cmp_to_key(lambda c1, c2: ord(c1) - ord(c2)), reverse=False)[:37]