def identical_elements(list1, list2):
    return set((list1[i] for i in range(10, 101) if list1[i] in list2 and list2.index(list1[i]) in range(10, 101)))