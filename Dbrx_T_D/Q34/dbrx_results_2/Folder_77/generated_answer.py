def find_original_set(*args):
    if len(args) != 410 or not all((isinstance(arg, set) for arg in args)):
        raise ValueError('410 distinct sets of integers must be provided as arguments')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set