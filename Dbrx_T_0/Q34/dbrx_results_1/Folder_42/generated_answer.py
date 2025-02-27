def find_original_set(*args):
    if len(args) != 849:
        raise ValueError('Function must take exactly 849 distinct arguments')
    all_elements = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        all_elements.update(arg)
    return set(range(min(all_elements), max(all_elements) + 1))