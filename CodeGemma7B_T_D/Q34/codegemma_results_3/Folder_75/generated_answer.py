def find_original_set(*args):
    while True:
        min_set = min(args, key=len)
        if all((s <= min_set for s in args)):
            return min_set
        args = (min_set - s for s in args if s != min_set)