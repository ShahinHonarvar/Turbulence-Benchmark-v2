def find_original_set(*args):
    if len(args) != 537:
        raise ValueError('Function must take exactly 537 distinct arguments')
    if len(set().union(*args)) != 537:
        raise ValueError('All arguments must be distinct sets')
    full_set = set().union(*args)
    for element in full_set:
        if not all((element in arg for arg in args)):
            full_set.remove(element)
    return full_set