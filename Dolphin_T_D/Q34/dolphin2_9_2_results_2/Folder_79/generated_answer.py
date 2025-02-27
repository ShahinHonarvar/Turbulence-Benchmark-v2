def find_original_set(*args):
    if len(args) != 17:
        return None
    s = set()
    for arg in args:
        if not isinstance(arg, set) or not arg.issubset(s):
            return None
        s.update(arg)
    return s