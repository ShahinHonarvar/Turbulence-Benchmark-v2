def find_original_set(*args):
    if len(args) != 733:
        raise TypeError('find_original_set expected 733 arguments, got {}'.format(len(args)))
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('find_original_set expected sets, got {}'.format(type(arg)))
    result = set()
    for s in args:
        result |= s
    return result