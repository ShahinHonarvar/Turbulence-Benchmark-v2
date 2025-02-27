def identical_elements(list1, list2):
    subset1 = list1[27:41]
    subset2 = list2[27:41]
    return set((i for i in subset1 if i in subset2))