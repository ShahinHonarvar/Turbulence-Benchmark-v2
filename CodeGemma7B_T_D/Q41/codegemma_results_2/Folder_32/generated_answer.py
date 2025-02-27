def identical_elements(l1, l2):
    return set((a for a in l1[21:97] for b in l2[21:97] if a == b))