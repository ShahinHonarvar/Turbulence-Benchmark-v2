def identical_elements(list1, list2):
    return set((x for x in list1[37:52] for y in list2[37:52] if x == y))