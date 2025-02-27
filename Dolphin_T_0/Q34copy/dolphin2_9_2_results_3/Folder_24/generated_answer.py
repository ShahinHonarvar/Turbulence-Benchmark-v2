def find_original_set(*args):
    return_set = set()
    for item in args:
        return_set = return_set.union(item)
    return return_set