def find_original_set(*args):
    a, b, c, d = args
    return min(a | b | c | d, key=len)