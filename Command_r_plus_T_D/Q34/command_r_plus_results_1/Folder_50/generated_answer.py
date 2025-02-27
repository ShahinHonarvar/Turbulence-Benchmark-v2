def find_original_set(*args):
    if len(args) != 99:
        raise ValueError('Exactly 99 arguments are required.')
    if len(set((id(s) for s in args))) != 99:
        raise ValueError('All arguments must be distinct sets.')
    result = set.union(*args)
    for s in args:
        if not result.issuperset(s):
            raise ValueError('The smallest set does not exist.')
    return result