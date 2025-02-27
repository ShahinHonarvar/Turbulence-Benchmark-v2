def find_original_set(*args):
    for s in itertools.product(*args):
        if all((x.issubset(s) for x in args)):
            return s