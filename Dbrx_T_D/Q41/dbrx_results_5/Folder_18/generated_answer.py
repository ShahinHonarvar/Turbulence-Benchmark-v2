def identical_elements(list1, list2):
    return set((list1[i] for i in range(35, 50) if list1[i] == list2[i] and list1[i] is not None))