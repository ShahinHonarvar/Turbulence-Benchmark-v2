def find_original_set(*args):
    max_set = set()
    for set_ in args:
        max_set.update(set_)
    return max_set