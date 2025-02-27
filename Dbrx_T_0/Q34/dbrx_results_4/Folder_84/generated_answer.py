def find_original_set(*args):
    if len(args) != 132:
        raise ValueError('Function must take exactly 132 distinct arguments')
    for arg in args:
        if not all((elem in arg for elem in arg)):
            raise ValueError('All arguments must be sets')
        if not all((isinstance(i, int) for i in arg)):
            raise ValueError('All elements in the sets must be integers')
    result = set()
    for arg in args:
        result.update(arg)
    return result