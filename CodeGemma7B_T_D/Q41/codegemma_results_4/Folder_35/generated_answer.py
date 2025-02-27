def identical_elements(list_a, list_b):
    return set((a for a in list_a[30:49] for b in list_b[30:49] if a == b))