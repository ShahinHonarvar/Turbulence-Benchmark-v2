def identical_elements(list_a, list_b):
    return set((a for a in list_a[62:93] for b in list_b[62:93] if a == b))