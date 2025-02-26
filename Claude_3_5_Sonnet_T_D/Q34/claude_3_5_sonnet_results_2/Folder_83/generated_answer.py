def find_original_set(*args):
    if len(args) != 64 or any((not isinstance(arg, set) for arg in args)):
        raise ValueError('Function requires exactly 64 distinct set arguments')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set