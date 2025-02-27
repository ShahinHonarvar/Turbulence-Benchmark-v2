def find_original_set(*args):
    result = set()
    for argument in args:
        result.update(argument)
    return result