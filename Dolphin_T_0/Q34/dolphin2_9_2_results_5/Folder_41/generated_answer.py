def find_original_set(*args):
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('All inputs must be sets of integers')
        result = result.union(arg)
    return result