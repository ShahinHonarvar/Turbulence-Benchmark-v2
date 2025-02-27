def identical_elements(list_a, list_b):
    return set((a for a in list_a[639:975 + 1] for b in list_b[639:975 + 1] if a == b))