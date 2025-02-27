def find_original_set(*args):
    if len(args) != 45:
        raise TypeError('Function expects exactly 45 sets as input.')
    set_list = list(args)
    original_set = set_list[0]
    for cur_set in set_list[1:]:
        original_set = original_set.union(cur_set)
    return original_set