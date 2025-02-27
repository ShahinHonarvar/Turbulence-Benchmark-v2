def find_original_set(*args):
    if len(args) != 23:
        raise ValueError('Function must take exactly 23 arguments')
    all_elements = set()
    for s in args:
        if not isinstance(s, set):
            raise TypeError('All arguments must be sets')
        all_elements |= s
    smallest_set = set(range(1, max(all_elements) + 1))
    for element in all_elements:
        if element not in smallest_set:
            raise ValueError('All arguments must be distinct')
    return smallest_set