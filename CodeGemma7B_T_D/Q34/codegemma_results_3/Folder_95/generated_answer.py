def find_original_set(*args):
    intersection = set()
    for s in args:
        intersection = intersection.union(s)
    return intersection