def find_original_set(*args):
    sets = list(args)
    result = set()
    for subset in sets:
        if result.issubset(subset):
            pass
        else:
            result = result.union(subset)
    return result