def identical_elements(list_a, list_b):
    set_a = set(list_a[80:201])
    set_b = set(list_b[80:201])
    return set_a.intersection(set_b)