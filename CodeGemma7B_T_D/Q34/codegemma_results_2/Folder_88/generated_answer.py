def find_original_set(*args):
    """To minimize the original set,
      we may assume that the smallest argument is the original set."""
    min_set = min(args)
    "For each argument 's',\n      we'll find the union of 's' and 'min_set'."
    for s in args:
        min_set |= s
    'Return the result.'
    return min_set