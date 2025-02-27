def find_original_set(*args):
    result = set()
    for a in args:
        result = result.union(a)
    return result