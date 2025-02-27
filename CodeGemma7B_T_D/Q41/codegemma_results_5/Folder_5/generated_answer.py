def identical_elements(list1, list2):
    return set((x for x in list1[8:10] for y in list2[8:10] if x == y)) or set()