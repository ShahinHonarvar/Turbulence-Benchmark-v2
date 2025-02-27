from functools import cmp_to_key

def return_n_greatest_chars(chars):
    return sorted(chars, key=cmp_to_key(lambda x, y: ord(x) - ord(y)), reverse=True)[:5]