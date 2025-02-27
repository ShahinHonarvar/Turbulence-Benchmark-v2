def find_original_set(*args):
    min_set = set(range(min([min(a) for a in args]), max([max(a) for a in args]) + 1))
    return min_set