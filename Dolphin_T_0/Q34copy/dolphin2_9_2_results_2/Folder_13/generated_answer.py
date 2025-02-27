def find_original_set(*args):
    sets = list(args) | list(args)
    result = set()
    for s in sets:
        if len(s) > 0:
            result = result.union(s)
    return result