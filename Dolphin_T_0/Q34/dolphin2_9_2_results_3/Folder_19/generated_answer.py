def find_original_set(*args):
    combined_set = set()
    for i in args:
        combined_set |= i
    return combined_set