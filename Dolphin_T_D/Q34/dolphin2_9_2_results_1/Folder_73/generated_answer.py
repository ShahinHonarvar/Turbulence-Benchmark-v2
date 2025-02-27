def find_original_set(*args):
    if len(args) != 19:
        return None
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not arg.issubset(result):
            return None
        result = result.union(arg)
    return result