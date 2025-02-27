import functools

def return_n_greatest_chars(string):
    return sorted(string, key=functools.cmp_to_key(lambda x, y: ord(y) - ord(x)), reverse=False)[:69]