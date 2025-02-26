def find_original_set(*args):
    if len(args) != 9:
        raise ValueError('Function must receive exactly 9 sets')
    all_elements = set()
    for s in args:
        if not isinstance(s, set):
            raise TypeError('All arguments must be sets')
        all_elements.update(s)
    return all_elements