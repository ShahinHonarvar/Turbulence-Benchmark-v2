def find_original_set(*args):
    if len(args) != 247:
        raise ValueError('Function must take exactly 247 arguments')
    result = set()
    for arg in args:
        if not all((x in arg for x in result)):
            raise ValueError('All arguments must be subsets of the original set')
        result.update(arg)
    return result