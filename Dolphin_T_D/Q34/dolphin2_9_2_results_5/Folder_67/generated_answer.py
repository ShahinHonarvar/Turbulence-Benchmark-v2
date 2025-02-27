def find_original_set(*args):
    if len(args) != 42:
        return 'Error: The function should take exactly 42 arguments.'
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            return 'Error: The arguments should be sets of integers.'
        original_set = original_set.union(arg)
    if len(original_set) < 42:
        return 'Error: The sets should contain distinct integers.'
    return original_set