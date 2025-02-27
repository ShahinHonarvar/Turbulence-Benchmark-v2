import functools

def return_n_greatest_chars(text):
    key = functools.cmp_to_key(lambda a, b: ord(b) - ord(a))
    return sorted(text, key=key)[:17]