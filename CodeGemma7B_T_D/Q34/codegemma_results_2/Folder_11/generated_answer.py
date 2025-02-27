def find_original_set(*args):
    sets = list(args)
    intersection = sets[0]
    for s in sets:
        intersection = s.intersection(intersection)
    return intersection