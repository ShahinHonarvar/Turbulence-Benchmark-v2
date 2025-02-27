def find_original_set(*args):
    result = set()
    for args_set in args:
        if args_set:
            result = result.union(args_set)
    return result