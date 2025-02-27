def find_original_set(*args):
    """
            This function finds the smallest set such that each of the given arguments is a subset of it.
            """
    original_set = min(args, key=len)
    unique_elements = set()
    for arg in args:
        unique_elements.update(arg)
    original_set.update(unique_elements)
    return original_set