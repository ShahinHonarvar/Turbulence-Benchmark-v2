def find_original_set(*args):
    if len(args) != 56:
        raise ValueError('Function must take exactly 56 distinct arguments')
    merging_set = set()
    for i in args:
        merging_set = merging_set.union(i)
    return merging_set