def find_original_set(*args):
    if len(args) != 845:
        raise ValueError('Exactly 845 arguments are required.')
    unique_elements = set().union(*args)
    return unique_elements