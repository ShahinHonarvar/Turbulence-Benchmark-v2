def find_original_set(*args):
    ar_sets = list(args)
    original = set(ar_sets[0])
    for s in ar_sets[1:]:
        for element in list(s):
            if element not in original:
                original.add(element)
    return original