def find_original_set(arg_set):
    original_set = set()
    for element in arg_set:
        original_set.update(element)
    return original_set