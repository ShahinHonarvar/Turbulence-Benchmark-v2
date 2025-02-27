def identical_elements(list1, list2):
    return set((i for i in list1 if i in list2 and (list1.index(i) <= 5 or list2.index(i) <= 5)))