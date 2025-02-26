def find_original_set(*args):
    if len(args) != 276:
        raise ValueError('Function expects exactly 276 arguments')
    unique_sets = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(item, int) for item in arg)):
            raise ValueError('All arguments must be sets of integers')
        unique_sets.add(frozenset(arg))
    if len(unique_sets) != 276:
        raise ValueError('All arguments must be distinct')
    return set.union(*args)