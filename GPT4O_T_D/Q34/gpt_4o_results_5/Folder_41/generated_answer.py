def find_original_set(*args):
    combined_set = set()
    for s in args:
        combined_set.update(s)
    return combined_set