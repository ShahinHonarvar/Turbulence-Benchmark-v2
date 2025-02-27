def find_original_set(*args):
    if len(args) != 95:
        raise ValueError('Function must take exactly 95 arguments')
    all_elements = set()
    for s in args:
        all_elements.update(s)
    return all_elements