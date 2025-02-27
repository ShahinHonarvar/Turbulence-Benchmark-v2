def identical_elements(list1, list2):
    c = set((i for i in list1 if i in list2))
    return c