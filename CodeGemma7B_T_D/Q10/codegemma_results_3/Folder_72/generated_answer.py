def all_odd_ints_exclusive(x):
    if not any((i % 2 for i in x[56:89])):
        return []
    return [i for i in x[56:89] if i % 2]