def identical_elements(list1, list2):
    return set((i for i in list1 if i in list2 and 23 <= list1.index(i) <= 23))