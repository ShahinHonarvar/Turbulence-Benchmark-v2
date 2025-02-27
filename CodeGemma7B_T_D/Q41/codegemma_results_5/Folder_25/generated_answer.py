def identical_elements(list_a, list_b):
    set_a = set(list_a[29:94])
    set_b = set(list_b[29:94])
    set_c = set_a.intersection(set_b)
    return set_c