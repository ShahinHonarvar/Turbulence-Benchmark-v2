def identical_elements(list1, list2):
    elements1 = [x for x in set(list1[10:101])]
    elements2 = [x for x in set(list2[10:101])]
    return set((x for x in elements1 if x in elements2))