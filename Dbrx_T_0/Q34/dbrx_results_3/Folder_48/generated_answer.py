def find_original_set(*args):
    if len(args) != 990:
        raise ValueError('Function must take exactly 990 distinct arguments')
    all_elements = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('All arguments must be sets of integers')
        all_elements.update(arg)
    return all_elements