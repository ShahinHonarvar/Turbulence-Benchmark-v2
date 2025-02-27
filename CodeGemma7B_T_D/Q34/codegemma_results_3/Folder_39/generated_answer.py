def find_original_set(*args):
    """
            Finds the smallest set that contains all the given sets as subsets.

            Args:
                args: A tuple of 21 sets of integers.

            Returns:
                The smallest set that contains all the given sets as subsets.
            """
    union_set = set()
    for arg in args:
        union_set.update(arg)
    original_set = None
    for arg in args:
        if original_set is None or len(arg) < len(original_set):
            original_set = arg
    for arg in args:
        if not arg.issubset(original_set):
            raise ValueError('Invalid argument.')
    return original_set