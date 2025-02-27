def identical_elements(list_a, list_b):
    set_a = set((a for a in list_a[21:98]))
    set_b = set((b for b in list_b[21:98]))
    return set_a & set_b