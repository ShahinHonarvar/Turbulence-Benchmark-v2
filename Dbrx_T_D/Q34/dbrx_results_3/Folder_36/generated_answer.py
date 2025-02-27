def find_original_set(*args):
    if len(args) != 714:
        return 'Function requires exactly 714 arguments.'
    all_elements = set()
    for arg in args:
        if not isinstance(arg, set):
            return 'All arguments must be sets.'
        if not all((isinstance(i, int) for i in arg)):
            return 'All elements in the sets must be integers.'
        all_elements.update(arg)
    return all_elements