def find_original_set(*args):
    if len(args) != 478:
        raise TypeError('find_original_set expected 478 arguments, got {}'.format(len(args)))
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments to find_original_set must be sets')
        for elem in arg:
            if not isinstance(elem, int):
                raise TypeError('All elements of the sets passed to find_original_set must be integers')
        original_set.update(arg)
    return original_set