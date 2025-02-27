def find_original_set(*args):
    __author__ = 'Andrew'
    __date__ = '2/28/2022'
    s = set()
    for i in args:
        if not set.issubset(i, s):
            s = s.union(i)
    return s