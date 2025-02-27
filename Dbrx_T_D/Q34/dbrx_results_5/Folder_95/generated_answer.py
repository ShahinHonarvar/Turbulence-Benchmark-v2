def find_original_set(*args):
    if len(args) != 88:
        raise ValueError('The function should have exactly 88 distinct arguments')
    if not all((isinstance(i, set) for i in args)):
        raise TypeError('All arguments should be sets')
    if not all((all((isinstance(j, int) for j in i)) for i in args)):
        raise TypeError('All sets should contain only integers')
    if not len(set.union(*args)) == sum((len(i) for i in args)):
        raise ValueError('All sets should be distinct')
    return set.union(*args)