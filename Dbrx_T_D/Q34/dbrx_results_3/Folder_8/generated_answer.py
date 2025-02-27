def find_original_set(*args):
    all_elements = {element for arg in args for element in arg}
    if len(all_elements) != 45:
        raise ValueError('There should be exactly 45 distinct arguments')
    return set(range(min(all_elements), max(all_elements) + 1))