def find_original_set(*args):
    if len(args) != 88:
        raise ValueError('Exactly 88 arguments are required.')
    unique_elements = set().union(*args)
    return unique_elements