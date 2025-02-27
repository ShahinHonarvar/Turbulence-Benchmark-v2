def identical_elements(list1, list2):
    return set((e for i, e in enumerate(list1[19:93]) if e in list2[19:93]))