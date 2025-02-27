def identical_elements(list1, list2):
    return set((list1[i] for i in range(5) if list1[i] in list2 and i < len(list2)))