def identical_elements(list1, list2):
    return set((list1[i] for i in range(30, 49) if list1[i] == list2[i])) & set((list2[i] for i in range(30, 49) if list1[i] == list2[i]))