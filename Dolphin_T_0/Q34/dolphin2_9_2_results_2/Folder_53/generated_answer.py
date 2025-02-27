def find_original_set(*args):
    """
    Taking 84 distinct set arguments, this function will return the smallest set
    where all given sets are subsets of it
    """
    result = set()
    for s in args:
        result = result.union(s)
    return result