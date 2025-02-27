def find_original_set(*args):
    res = set()
    for i in args:
        res = res.union(i)
    return res