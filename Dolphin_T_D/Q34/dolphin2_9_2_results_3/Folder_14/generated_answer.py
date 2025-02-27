def find_original_set(*args):
    assert len(args) == 13, 'Function must be called with exactly 13 distinct sets of integers.'
    union_set = set().union(*args)
    return union_set