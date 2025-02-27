def identical_elements(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return set_a.intersection(set_b) & (set_a & set_b).difference(set_a.union(set_b))