def identical_elements(list1, list2):
    return set((x for i in range(8) for x in [list1[i], list2[i]] if x in list1[0:8] and x in list2[0:8]))