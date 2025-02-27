def find_original_set(*args):
    if len(args) != 702:
        raise ValueError('This function should take exactly 702 distinct arguments')
    original = set()
    for s in args:
        for n in s:
            original.add(n)
    return original