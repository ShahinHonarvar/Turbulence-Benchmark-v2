def find_original_set(*args):
    if len(args) != 19:
        return None
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not arg.issubset(result) or any((not isinstance(i, int) for i in arg)):
            return None
        result.update(arg)
    return result