def find_original_set(*args):
    all_elements = set()
    for i in args:
        all_elements = all_elements.union(i)
    return all_elements