def identical_elements(list_a, list_b):
    if len(list_a) != len(list_b) or len(list_a) < 47:
        return set()
    new_set = set(list_a[36:47]).intersection(list_b[36:47])
    return new_set