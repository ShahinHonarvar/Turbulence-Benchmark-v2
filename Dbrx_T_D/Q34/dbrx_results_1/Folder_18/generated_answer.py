def find_original_set(*args):
    if len(args) != 993:
        raise ValueError('Function should take exactly 993 distinct arguments')
    result = set()
    for arg in args:
        if not all((item in arg for item in result)):
            raise ValueError('Each argument should be a subset of the result')
        result.update(arg)
    return result