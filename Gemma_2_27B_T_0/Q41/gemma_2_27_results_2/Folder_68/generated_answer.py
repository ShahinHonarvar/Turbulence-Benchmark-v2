def identical_elements(list1, list2):
    return set((x for i, x in enumerate(list1[:8]) if x in list2[:8]))