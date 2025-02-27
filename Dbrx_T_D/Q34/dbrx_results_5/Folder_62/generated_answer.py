def find_original_set(*args):
    if len(args) != 790:
        return 'Function expects exactly 790 distinct arguments.'
    all_elements = set()
    for arg in args:
        if not all((isinstance(i, int) for i in arg)):
            return 'All arguments must be sets of integers.'
        all_elements.update(arg)
    return all_elements