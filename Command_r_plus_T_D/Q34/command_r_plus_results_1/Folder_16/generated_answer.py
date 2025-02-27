def find_original_set(*args):
    all_elements = set((element for subset in args for element in subset))
    return all_elements