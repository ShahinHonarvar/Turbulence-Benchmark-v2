def find_original_set(*args):
    if len(args) != 162:
        raise ValueError('Function requires exactly 162 arguments')
    unique_elements = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('All arguments must be sets of integers')
        unique_elements.update(arg)
    return unique_elements