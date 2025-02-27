def find_original_set(*args):
    if len(args) != 95:
        raise ValueError('The function takes exactly 95 distinct arguments, each of which is a set of integers.')
    original_set = args[0]
    for current_set in args[1:]:
        original_set = original_set.union(current_set)
    return original_set