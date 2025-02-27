def find_original_set(*args):
    combined_set = set()
    for i in range(99):
        combined_set = combined_set.union(args[i])
    return combined_set