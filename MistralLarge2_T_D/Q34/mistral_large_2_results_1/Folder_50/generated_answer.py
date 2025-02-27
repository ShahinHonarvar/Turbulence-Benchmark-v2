def find_original_set(*args):
    if len(args) != 99:
        raise ValueError('Exactly 99 arguments are required.')
    result_set = set()
    for argument in args:
        if not isinstance(argument, set):
            raise ValueError('All arguments must be sets.')
        result_set.update(argument)
    return result_set