def find_original_set(*args):
    if len(args) != 87:
        raise ValueError('Function requires exactly 87 arguments.')
    if len(set(args)) != 87:
        raise ValueError('All arguments must be distinct sets.')
    result = set(args[0])
    for arg in args[1:]:
        result = result.union(arg)
    return result