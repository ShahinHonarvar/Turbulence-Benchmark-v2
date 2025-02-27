def find_original_set(*args):
    all_elements = set()
    for s in args:
        all_elements.update(s)
    return all_elements