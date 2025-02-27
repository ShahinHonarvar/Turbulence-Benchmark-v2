def identical_elements(list_a, list_b):
    set_a = set(list_a[30:49])
    set_b = set(list_b[30:49])
    return set_a.intersection(set_b)