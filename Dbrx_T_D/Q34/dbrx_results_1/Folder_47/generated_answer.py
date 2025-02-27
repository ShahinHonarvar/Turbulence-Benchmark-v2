def find_original_set(*args):
    if len(args) != 77:
        raise ValueError('Function must take exactly 77 distinct arguments')
    union_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('All arguments must be sets of integers')
        union_set.update(arg)
    return union_set