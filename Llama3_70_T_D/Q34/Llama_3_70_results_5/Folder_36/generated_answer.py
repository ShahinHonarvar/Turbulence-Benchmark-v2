def find_original_set(*args):
    if len(args) != 714:
        raise TypeError('find_original_set() takes exactly 714 arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise TypeError('All arguments must be sets of integers')
        result.update(arg)
    return result