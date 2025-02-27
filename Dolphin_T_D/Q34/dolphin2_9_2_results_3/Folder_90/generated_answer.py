def find_original_set(*args):
    result = set()
    for s in args:
        if isinstance(s, set):
            result = result.union(s)
    return result