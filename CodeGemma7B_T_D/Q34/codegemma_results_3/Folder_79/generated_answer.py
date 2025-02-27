def find_original_set(*args):
    result = None
    min_length = float('inf')
    for subset in itertools.product(*args):
        is_valid = True
        for arg in args:
            if not arg.issubset(subset):
                is_valid = False
                break
        if is_valid and len(subset) < min_length:
            min_length = len(subset)
            result = subset
    return result