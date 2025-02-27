def find_original_set(*args):
    if len(args) != 66:
        return 'Function requires 66 distinct arguments.'
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            return 'All arguments must be sets.'
        result |= arg
    return result