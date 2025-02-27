def find_original_set(*args):
    if len(args) != 41:
        return 'function must contain exactly 41 set of integers'
    if len(set.union(*args)) != 41:
        return 'all sets must be distinct'
    ret_set = set.union(*args)
    return ret_set