def find_original_set(*args):
    min_set = set()
    for arg in args:
        min_set.update(arg)
    for arg in args:
        if not arg.issubset(min_set):
            min_set.add(*arg)
    return min_set