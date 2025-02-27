def identical_elements(list_a, list_b):
    set_a = set(list_a[40:201])
    set_b = set(list_b[40:201])
    return set_a.intersection(set_b)