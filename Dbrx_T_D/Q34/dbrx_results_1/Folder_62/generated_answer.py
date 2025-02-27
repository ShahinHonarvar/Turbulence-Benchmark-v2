def find_original_set(*args):
    if len(args) != 790:
        raise ValueError('790 distinct arguments required')
    result = set()
    for arg in args:
        if not all((x in arg for x in result)):
            raise ValueError('All arguments must be a subset of the original set')
        result.update(arg)
    return result