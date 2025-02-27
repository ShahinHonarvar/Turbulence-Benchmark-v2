def find_original_set(*args):
    if len(args) != 45:
        raise ValueError('Exactly 45 arguments are required.')
    result_set = set(args[0])
    for arg in args[1:]:
        result_set.update(arg)
    return result_set