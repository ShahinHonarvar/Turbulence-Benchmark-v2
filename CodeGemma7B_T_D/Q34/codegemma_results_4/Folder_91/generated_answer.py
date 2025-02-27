from functools import reduce

def find_original_set(a, b, c, d, e):
    return reduce(lambda x, y: x.union(y), (a, b, c, d, e))