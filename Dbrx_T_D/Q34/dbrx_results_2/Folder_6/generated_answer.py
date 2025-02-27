def find_original_set(*args):
    if len(args) != 276:
        raise ValueError('Function must take exactly 276 arguments')
    result_set = set()
    for arg in args:
        if not all((elem in arg for elem in arg)):
            raise ValueError('All arguments must be sets of integers')
        result_set.update(arg)
    return result_set