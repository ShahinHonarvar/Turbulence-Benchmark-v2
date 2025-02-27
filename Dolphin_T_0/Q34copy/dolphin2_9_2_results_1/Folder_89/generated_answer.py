def find_original_set(*args):
    """
    This function takes 37 distinct arguments, each of which is a set of integers.
    The function should return the smallest set such that each of the given arguments
    is a subset of it.
    """
    if len(args) != 37:
        raise ValueError('This function expects exactly 37 arguments.')
    result = set()
    for i in args:
        result = result.union(i)
    return result