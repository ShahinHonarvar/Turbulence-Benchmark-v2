def find_original_set(*args):
    if len(args) != 990:
        raise ValueError('Function takes exactly 990 arguments')
    if len(set.union(*args)) != sum(map(len, args)):
        raise ValueError('Not all arguments are distinct')
    return set.union(*args)