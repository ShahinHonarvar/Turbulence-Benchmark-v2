def identical_elements(list_a, list_b):
    set_a = set(list_a[30:88])
    set_b = set(list_b[30:88])
    same_elements = set_a.intersection(set_b)
    return same_elements