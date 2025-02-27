def find_original_set(*args):
    if len(args) != 47:
        raise ValueError('Invalid number of arguments.')
    result = {}
    for i in range(47):
        for item in args[i]:
            result[item] = True
    return set(result.keys())