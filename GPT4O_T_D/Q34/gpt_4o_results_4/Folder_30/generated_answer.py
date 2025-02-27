def find_original_set(*args):
    merged_set = set()
    for subset in args:
        merged_set.update(subset)
    return merged_set