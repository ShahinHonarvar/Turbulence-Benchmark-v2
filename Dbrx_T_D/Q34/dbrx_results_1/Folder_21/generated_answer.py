def find_original_set(*args):
    if len(args) != 851:
        raise ValueError('Exactly 851 distinct arguments should be provided')
    if len(set().union(*args)) != 851:
        raise ValueError('All arguments should be distinct')
    result = set().union(*args)
    for arg in args:
        if arg - result:
            raise ValueError('Every provided set should be a subset of the result')
    return result