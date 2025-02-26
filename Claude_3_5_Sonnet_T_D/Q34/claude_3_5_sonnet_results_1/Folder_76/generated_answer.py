def find_original_set(*args):
    if len(args) != 247:
        raise ValueError('Function must receive exactly 247 arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise ValueError('All arguments must be sets of integers')
        original_set.update(arg)
    return original_set