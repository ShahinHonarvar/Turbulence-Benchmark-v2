def find_original_set(*args):
    if len(args) != 247:
        raise ValueError('The function should take exactly 247 arguments')
    min_set = set()
    for s in args:
        if not s.issubset(min_set):
            min_set = s
    return min_set