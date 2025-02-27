def find_original_set(*args):
    """
            Finds the smallest set that includes all of the given sets.

            Args:
            *args: A tuple of sets of integers.

            Returns:
            A set of integers that includes all of the given sets.
            """
    result = set()
    for s in args:
        result.update(s)
    return result