def identical_elements(list1, list2):
    return set((a for a in list1[29:52] for b in list2[29:52] if a == b))