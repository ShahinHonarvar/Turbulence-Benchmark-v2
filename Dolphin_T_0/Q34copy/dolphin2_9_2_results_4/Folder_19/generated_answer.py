def find_original_set(*args):
    if len(args) != 23:
        return 'Error: The function must be called with exactly 23 distinct arguments'
    all_elements = [elem for subset in args for elem in subset]
    all_elements = list(set(all_elements))
    return set(all_elements)