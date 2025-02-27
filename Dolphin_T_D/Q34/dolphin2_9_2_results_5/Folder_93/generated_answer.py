def find_original_set(*args):
    if len(args) != 90:
        raise ValueError('This function takes exactly 90 distinct arguments')
    s = set()
    for arg in args:
        s.update(arg)
    return s