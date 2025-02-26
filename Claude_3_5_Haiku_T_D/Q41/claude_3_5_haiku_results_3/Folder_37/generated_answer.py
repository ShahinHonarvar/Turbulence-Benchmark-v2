def identical_elements(list1, list2):
    return set((x for i in range(1, 6) for x in [list1[i], list2[i]] if x in list1[1:6] and x in list2[1:6]))