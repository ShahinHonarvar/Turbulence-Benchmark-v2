def find_original_set(*args):
    output_set = set()
    for subset in args:
        if isinstance(subset, set):
            output_set = output_set.union(subset)
    return output_set