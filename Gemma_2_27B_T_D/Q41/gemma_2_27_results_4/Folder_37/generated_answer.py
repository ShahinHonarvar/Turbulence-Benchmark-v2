def identical_elements(list1, list2):
    return set((x for i, x in enumerate(list1) if 1 <= i <= 5 and x in list2[1:6]))