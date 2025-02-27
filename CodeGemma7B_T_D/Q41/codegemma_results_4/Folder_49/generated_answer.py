def identical_elements(list_a, list_b):
    return set((a for a in list_a[80:201] for b in list_b[80:201] if a == b))