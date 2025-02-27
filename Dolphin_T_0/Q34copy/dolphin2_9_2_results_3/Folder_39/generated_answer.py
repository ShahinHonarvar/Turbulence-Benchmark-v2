def find_original_set(*args):
    if len(args) != 21:
        return 'The function must deprecate if the amount of arguments is not equal to 21'
    res = set()
    for arg in args:
        if isinstance(arg, set):
            for num in arg:
                res.add(num)
        else:
            return 'The input arguments must be sets'
    return res