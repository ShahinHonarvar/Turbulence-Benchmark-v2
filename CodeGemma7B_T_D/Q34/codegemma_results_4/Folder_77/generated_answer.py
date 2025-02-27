def find_original_set(*args):
    pool = set()
    for s in args:
        pool.update(s)
    return pool