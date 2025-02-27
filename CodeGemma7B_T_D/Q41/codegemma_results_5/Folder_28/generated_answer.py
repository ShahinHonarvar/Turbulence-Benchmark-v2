def identical_elements(list_a, list_b):
    set_a = set(list_a[62:64])
    set_b = set(list_b[62:64])
    return set_a.intersection(set_b)