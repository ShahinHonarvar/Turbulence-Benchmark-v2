def find_original_set(*args):
    if len(args) != 40:
        raise ValueError('The function must take exactly 40 arguments.')
    for i in range(len(args)):
        for j in range(i + 1, len(args)):
            if args[i] == args[j]:
                raise ValueError('All arguments must be distinct sets.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set