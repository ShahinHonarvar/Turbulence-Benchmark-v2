def identical_elements(list_a, list_b):
    set_a = set(list_a[28:33])
    set_b = set(list_b[28:33])
    return set_a.intersection(set_b)