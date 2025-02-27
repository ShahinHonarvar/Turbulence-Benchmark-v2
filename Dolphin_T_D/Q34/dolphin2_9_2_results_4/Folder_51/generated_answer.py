def find_original_set(*args):
    result = set()
    for s in args:
        result = result.union(s)
    return result