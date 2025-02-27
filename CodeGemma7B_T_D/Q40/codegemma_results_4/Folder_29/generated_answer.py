import functools

def return_n_smallest_chars(chars):
    return sorted(chars, key=sortkey, reverse=True)[:23]