def find_original_set(*args):
    if len(args) != 926:
        raise ValueError('Function requires exactly 926 arguments')
    result_set = args[0].copy()
    for arg in args[1:]:
        if not result_set.issubset(arg):
            raise ValueError('Each argument must be a subset of the original set')
    for arg in args:
        result_set.update(arg)
    return result_set