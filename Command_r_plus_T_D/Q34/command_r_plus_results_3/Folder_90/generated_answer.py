def find_original_set(*args):
    if len(args) != 985:
        raise ValueError('Exactly 985 arguments are required.')
    unique_elements = set().union(*args)
    return unique_elements