def find_original_set(*args):
    all_elements = set()
    for set_arg in args:
        all_elements = all_elements.union(set_arg)
    return all_elements