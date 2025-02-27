def find_original_set(*args):
    if len(args) != 849 or len(args) != len(set(args)):
        raise ValueError('The function should take exactly 849 distinct arguments')
    return {value for s in args for value in s}