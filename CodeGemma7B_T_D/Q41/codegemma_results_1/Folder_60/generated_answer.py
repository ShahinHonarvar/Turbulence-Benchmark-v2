def identical_elements(list_a, list_b):
    return set((x for x in list_a[75:86] for y in list_b[75:86] if x == y))