def identical_elements(list_a, list_b):
    set_a, set_b = (set(list_a[82:87]), set(list_b[82:87]))
    return set_a & set_b