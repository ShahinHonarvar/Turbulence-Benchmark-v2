def find_original_set(*args):
    assert len(args) == 18 and len(set(map(len, args))) == 1, 'Invalid number of sets or sets of distinct length'
    return set.union(*args)