def find_original_set(*args):
    if len(args) != 53:
        raise ValueError('The function requires 53 distinct set arguments.')
    res = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All function arguments should be sets.')
        if res == set():
            res = res.union(arg)
        else:
            res = res.intersection(arg)
    return res