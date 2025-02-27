def find_original_set(*args):
    combined_set = set()
    for arg in args:
        combined_set = combined_set.union(arg)
    return combined_set