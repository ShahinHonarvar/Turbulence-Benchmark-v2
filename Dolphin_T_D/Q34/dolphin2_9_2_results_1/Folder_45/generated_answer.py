def find_original_set(*args):
    all_elements = set()
    for set_arg in args:
        all_elements.update(set_arg)
    return all_elements