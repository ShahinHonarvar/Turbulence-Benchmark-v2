def find_original_set(*args):
    if len(args) != 247:
        raise ValueError('Function requires exactly 247 arguments')
    original_set = set()
    for arg in args:
        if not all((item in arg for item in original_set)):
            raise ValueError('Each argument must be a subset of the original set')
        original_set.update(arg)
    return original_set