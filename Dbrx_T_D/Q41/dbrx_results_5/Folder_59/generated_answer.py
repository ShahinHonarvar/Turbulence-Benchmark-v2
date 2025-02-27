def identical_elements(list1, list2):
    return set((list1[i] for i in range(9) if list1[i] == list2[i])) & set(list1) & set(list2)