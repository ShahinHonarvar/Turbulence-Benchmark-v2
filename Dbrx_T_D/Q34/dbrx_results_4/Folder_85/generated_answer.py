def find_original_set(*args):
    if len(args) != 85 or not all((isinstance(arg, set) for arg in args)):
        raise ValueError('Exactly 85 distinct sets of integers must be provided.')
    result = set()
    for arg in args:
        result.update(arg)
    return result