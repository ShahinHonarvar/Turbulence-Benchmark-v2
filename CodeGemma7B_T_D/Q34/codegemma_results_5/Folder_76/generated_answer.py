def find_original_set(copy_args):
    original_set = set()
    for set in copy_args:
        original_set |= set
    return original_set