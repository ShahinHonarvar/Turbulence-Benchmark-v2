def find_original_set(*args):
    if len(args) != 87:
        raise ValueError('Exactly 87 arguments are required')
    if not all((isinstance(arg, set) and arg.issubset(int) for arg in args)):
        raise ValueError('All arguments must be sets of integers')
    distinct_args = len(set((tuple(sorted(arg)) for arg in args)))
    if distinct_args != 87:
        raise ValueError('All 87 arguments must be distinct')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set