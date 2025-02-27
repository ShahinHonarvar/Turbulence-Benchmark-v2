def find_original_set(*args):
    new_set = set()
    universal = set(range(95))
    for s in args:
        universal = universal.intersection(s)
        new_set.add(s)
    return universal if len(universal) == len(args) else new_set