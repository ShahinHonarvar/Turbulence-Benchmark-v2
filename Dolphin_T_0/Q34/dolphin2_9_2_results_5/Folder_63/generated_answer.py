def find_original_set(*args):
    result = set([])
    for set_input in args:
        if len(set_input) != 0:
            result = result.union(set_input)
    return result