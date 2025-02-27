def find_original_set(*args):
    if len(args) != 51:
        raise ValueError("Function 'find_original_set' requires exactly 51 arguments")
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("Function 'find_original_set' requires arguments to be sets of integers")
        if not arg.issubset(result):
            result.update(arg)
    return result