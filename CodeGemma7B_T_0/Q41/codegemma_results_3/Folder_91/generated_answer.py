def identical_elements(list1, list2):
    return set((item for item in list1 for i in range(5) if list1[i] == list2[i]))