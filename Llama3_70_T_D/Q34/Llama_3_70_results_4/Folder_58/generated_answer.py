def find_original_set(*args):
    if len(args) != 733:
        raise TypeError('find_original_set() takes exactly 733 arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('all arguments to find_original_set() must be sets')
        result.update(arg)
    return result