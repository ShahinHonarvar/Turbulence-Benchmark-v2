def identical_elements(list1, list2):
    return set((x for x in list1 if x in list2 and 35 <= list1.index(x) <= 49 and (35 <= list2.index(x) <= 49)))