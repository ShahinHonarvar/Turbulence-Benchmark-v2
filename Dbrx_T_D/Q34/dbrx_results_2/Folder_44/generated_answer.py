def find_original_set(*args):
    all_elements = [element for arg in args for element in arg]
    if len(all_elements) != 926:
        raise ValueError('926 distinct arguments required')
    unique_elements = set(all_elements)
    for arg in args:
        if not unique_elements.issuperset(arg):
            return False
    return unique_elements