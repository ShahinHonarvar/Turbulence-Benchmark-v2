def find_original_set(*args):
    if len(args) != 828:
        raise ValueError('Function requires exactly 828 arguments')
    return set().union(*args)