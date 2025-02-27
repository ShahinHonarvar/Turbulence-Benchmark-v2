def find_original_set(*args):
    if len(args) != 41:
        raise ValueError('Function should take exactly 41 arguments')
    result_set = set()
    for arg in args:
        if not all((x in result_set for x in arg)):
            result_set.update(arg)
    return result_set