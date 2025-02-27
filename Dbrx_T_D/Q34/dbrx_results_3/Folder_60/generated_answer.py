def find_original_set(*args):
    if len(args) != 35:
        raise ValueError('Function must be called with exactly 35 distinct arguments.')
    union_set = set()
    for s in args:
        if not isinstance(s, set) or not all((isinstance(i, int) for i in s)):
            raise ValueError('Each argument must be a set of integers.')
        union_set.update(s)
    return union_set