def identical_elements(list_a, list_b):
    set_a = set(list_a[22:89])
    set_b = set(list_b[22:89])
    return set_a.intersection(set_b)