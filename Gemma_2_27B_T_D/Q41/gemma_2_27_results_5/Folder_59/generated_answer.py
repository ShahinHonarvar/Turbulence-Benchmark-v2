def identical_elements(list1, list2):
    return set((e for i in range(9) for e in [list1[i], list2[i]] if e in list2 and e in list1))