def identical_elements(list1, list2):
    return set((x for i, x in enumerate(list1[34:56]) if x in list2[34:56]))