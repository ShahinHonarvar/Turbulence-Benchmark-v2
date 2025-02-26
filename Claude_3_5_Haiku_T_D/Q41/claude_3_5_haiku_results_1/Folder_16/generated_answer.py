def identical_elements(list1, list2):
    return set((x for i, x in enumerate(list1) if 33 <= i <= 36 and x in list2[33:37]))