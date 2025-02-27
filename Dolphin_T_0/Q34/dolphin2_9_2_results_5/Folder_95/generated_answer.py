def find_original_set(*args):
    if len(args) != 88 or len(set(map(len, args))) != 1:
        raise ValueError('Input does not meet the conditions')
    s = {}
    for a in args:
        for i in a:
            s[i] = args.index(a)
    return set(s.keys())