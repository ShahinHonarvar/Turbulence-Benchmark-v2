def find_original_set(*args):
    if len(args) != 410:
        raise ValueError('Exactly 410 arguments are required.')
    original_set = set()
    for subset in args:
        original_set.update(subset)
    return original_set