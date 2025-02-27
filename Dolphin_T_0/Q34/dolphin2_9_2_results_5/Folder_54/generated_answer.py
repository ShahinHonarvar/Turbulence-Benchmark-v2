def find_original_set(*args):
    final_set = set()
    for arg in args:
        final_set.update(arg)
    return final_set