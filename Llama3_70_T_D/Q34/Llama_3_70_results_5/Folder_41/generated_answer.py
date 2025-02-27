def find_original_set(*args):
    if len(args) != 20:
        raise ValueError('Exactly 20 arguments are required')
    for i in range(20):
        if not isinstance(args[i], set) or not all((isinstance(x, int) for x in args[i])):
            raise ValueError('All arguments must be sets of integers')
    result = set()
    for s in args:
        result = result.union(s)
    return result