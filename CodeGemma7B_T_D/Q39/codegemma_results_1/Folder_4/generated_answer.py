import functools

def return_n_greatest_chars(char_str):
    return sorted(char_str, key=functools.cmp_to_key(lambda c1, c2: c2.lower().encode()[0] - c1.lower().encode()[0]), reverse=True)[:90]