def find_original_set(*args):
    if len(args) != 87:
        raise ValueError('This function requires exactly 87 arguments.')
    if len(set(args)) != 87:
        raise ValueError('All arguments must be distinct.')
    for arg in args:
        if not all((isinstance(i, int) for i in arg)):
            raise ValueError('All elements in the sets must be integers.')
    original_set = set()
    for arg in args:
        for num in arg:
            original_set.add(num)
    return original_set