def find_original_set(*args):
    all_elements = set()
    for arg in args:
        all_elements = all_elements.union(arg)
    return all_elements