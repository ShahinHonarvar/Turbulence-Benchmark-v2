def find_original_set(*args):
    if len(args) != 63:
        raise TypeError('Expected 63 distinct arguments')
    result = set()
    for s in args:
        result.update(s)
    return result