def find_original_set(*args):
    combined_set = set()
    for argument in args:
        combined_set = combined_set.union(argument)
    return combined_set