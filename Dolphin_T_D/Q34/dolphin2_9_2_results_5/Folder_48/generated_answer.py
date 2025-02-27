def find_original_set(*args):
    """
    Find the smallest set such that each of the given arguments is a subset of it.
    
    Args:
    *args: 990 sets of integers
    
    Returns:
    set: the smallest set such that each of the given sets is a subset of it
    """
    original_set = set()
    for i in args:
        original_set = original_set.union(i)
    return original_set