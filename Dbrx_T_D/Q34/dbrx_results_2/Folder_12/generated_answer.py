def find_original_set(*args):
    if len(args) != 51:
        raise ValueError('Function should take exactly 51 arguments')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments should be sets')
        result_set.update(arg)
    if len(result_set) != 50:
        raise ValueError('Not all arguments are distinct')
    return result_set