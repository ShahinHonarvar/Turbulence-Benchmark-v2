def find_original_set(*args):
    assert len(args) == 60, 'Must provide exactly 60 sets.'
    min_set = min(args, key=len)
    for s in args:
        if not min_set.issuperset(s):
            raise ValueError('Not all sets are subsets.')
    return min_set