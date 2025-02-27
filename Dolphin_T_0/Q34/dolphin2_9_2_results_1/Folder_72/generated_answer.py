def union_sets(*args):
    result = set()
    for s in args:
        result |= s
    return result