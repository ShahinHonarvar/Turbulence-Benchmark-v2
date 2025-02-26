def find_original_set(*args):
    if len(args) != 87:
        raise ValueError('Function requires exactly 87 arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(item, int) for item in arg)):
            raise ValueError('All arguments must be sets of integers')
        original_set.update(arg)
    return original_set