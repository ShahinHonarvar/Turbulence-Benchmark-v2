def identical_elements(list_a, list_b):
    set_a = set(list_a[6:7])
    set_b = set(list_b[6:7])
    return set_a.intersection(set_b)