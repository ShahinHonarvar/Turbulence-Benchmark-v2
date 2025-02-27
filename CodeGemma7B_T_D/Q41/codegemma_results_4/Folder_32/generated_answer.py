def identical_elements(list1, list2):
    return set((l1 for l1, l2 in zip(list1[21:98], list2[21:98]) if l1 == l2))