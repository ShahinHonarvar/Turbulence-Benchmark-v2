def identical_elements(list1, list2):
    return set((x for i in range(50, 55) for x in [list1[i], list2[i]] if x in list1[50:55] and x in list2[50:55]))