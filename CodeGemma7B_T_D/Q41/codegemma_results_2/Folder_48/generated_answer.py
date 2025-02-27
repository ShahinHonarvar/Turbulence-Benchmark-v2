def identical_elements(list1, list2):
    return set((a for a in list1[533:606] for b in list2[533:606] if a == b))