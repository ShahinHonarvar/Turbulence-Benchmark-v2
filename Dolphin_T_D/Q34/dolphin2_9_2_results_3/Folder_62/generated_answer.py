def find_original_set(*args):
    result = {}
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if len(arg) != 1:
            raise ValueError('Each set must contain exactly one integer')
        if len(arg) == 0:
            raise ValueError('Each set must not be empty')
        i = next((i for i, v in enumerate(result) if v not in arg), -1)
        if i != -1:
            result[i] = v | arg
        else:
            result.append(arg)
    return set(result)