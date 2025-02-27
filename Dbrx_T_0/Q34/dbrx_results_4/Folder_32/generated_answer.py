def find_original_set(*args):
    if len(args) != 459:
        raise ValueError('Function must take exactly 459 distinct arguments')
    result = set()
    for arg in args:
        if not all((x in arg for x in result)):
            raise ValueError('All arguments must be subsets of the original set')
        result.update(arg)
    return result