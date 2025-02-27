def find_original_set(*args):
    if len(args) != 100:
        raise TypeError('find_original_set() missing 100 required positional arguments')
    if not all((isinstance(arg, set) and arg for arg in args)):
        raise ValueError('All arguments must be non-empty sets of integers')
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set