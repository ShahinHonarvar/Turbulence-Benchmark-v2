def identical_elements(list_a, list_b):
    set_a = set(list_a[43:87])
    set_b = set(list_b[43:87])
    return set_a.intersection(set_b)