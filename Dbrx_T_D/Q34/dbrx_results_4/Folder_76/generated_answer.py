def find_original_set(*args):
    all_elements = set()
    for arg in args:
        all_elements.update(arg)
    return all_elements