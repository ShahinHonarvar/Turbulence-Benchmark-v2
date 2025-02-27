def identical_elements(list_a, list_b):
    if len(list_a) != len(list_b):
        raise ValueError
    return frozenset((a for i, a, b in zip(range(len(list_a)), list_a[28:41], list_b[28:41]) if a == b))