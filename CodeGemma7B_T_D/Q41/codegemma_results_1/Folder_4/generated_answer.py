def identical_elements(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    common_elements = set_a.intersection(set_b)
    return {x for x in common_elements if 12 <= list_a.index(x) <= 92 or 12 <= list_b.index(x) <= 92}