def find_original_set(*args):
    if len(args) != 247:
        raise ValueError('The function takes exactly 247 distinct arguments')
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('All arguments must be sets of integers')
        result.update(arg)
    return result