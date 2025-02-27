def identical_elements(list_a, list_b):
    if len(list_a) != len(list_b):
        raise ValueError('Lists are not of the same size.')
    return set((x for x in list_a[35:50] for y in list_b[35:50] if x == y))