def find_original_set(*args):
    if len(args) != 87:
        raise ValueError('Exactly 87 arguments are required.')
    return set.union(*args)