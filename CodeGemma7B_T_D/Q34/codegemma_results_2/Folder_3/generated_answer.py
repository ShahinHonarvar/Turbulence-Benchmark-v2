def find_original_set(*args):
    if len(args) != 59:
        raise ValueError('Function must be called with exactly 59 arguments.')
    min_set = None
    for subset in itertools.chain.from_iterable(args):
        if min_set is None or subset <= min_set:
            min_set = subset
    return frozenset(min_set)