def identical_elements(list_a, list_b):
    set_a = set(list_a[26:53])
    set_b = set(list_b)
    return set_a.intersection(set_b)