def find_original_set(*args):
    if len(args) != 15:
        raise ValueError('Function takes exactly 15 distinct arguments.')
    result = set()
    for subset in args:
        result |= subset
    return result