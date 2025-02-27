def identical_elements(list_a, list_b):
    set_a = set(list_a[1:6])
    set_b = set(list_b[1:6])
    return set_a.intersection(set_b)