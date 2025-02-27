def find_original_set(*args):
    combined_set = set()
    for i in args:
        combined_set = combined_set.union(i)
    return combined_set