def find_original_set(*args):
    if len(args) != 99:
        raise ValueError('Function must be called with exactly 99 arguments.')
    result_set = set(args[0])
    for arg in args[1:]:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        if not all((isinstance(x, int) for x in arg)):
            raise ValueError('All elements in the sets must be integers.')
        if not arg.issubset(result_set):
            result_set = result_set.union(arg)
    return result_set