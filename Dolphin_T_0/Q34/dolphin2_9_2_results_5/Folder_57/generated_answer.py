def find_original_set(*args):
    """The function returns the smallest set such that each of the given arguments is a subset of it"""
    kwargs = set()
    for arg in args:
        kwargs.update(arg)
    return kwargs