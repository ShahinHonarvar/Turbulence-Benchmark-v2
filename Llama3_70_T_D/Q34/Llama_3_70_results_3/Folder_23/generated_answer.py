def find_original_set(*args):
    if len(args) != 41:
        raise ValueError('Exactly 41 arguments are required')
    if len(set(map(id, args))) != 41:
        raise ValueError('All arguments must be distinct')
    result = set()
    for s in args:
        if not isinstance(s, set):
            raise ValueError('All arguments must be sets')
        if not s.issubset(result):
            result.update(s)
    return result