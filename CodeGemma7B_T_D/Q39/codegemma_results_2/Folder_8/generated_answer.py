import functools

def returning_n_greatest_chars(c):
    return sorted(c, key=functools.cmp_to_key(lambda a, b: ord(b) - ord(a)), reverse=True)[:83]