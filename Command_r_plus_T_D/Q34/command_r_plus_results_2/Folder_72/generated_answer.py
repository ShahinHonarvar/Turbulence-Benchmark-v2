def find_original_set(*args):
    if len(args) != 87:
        raise ValueError('Exactly 87 arguments are required.')
    if len(set(args)) != 87:
        raise ValueError('All arguments must be distinct.')
    original_set = set.union(*args)
    return original_set