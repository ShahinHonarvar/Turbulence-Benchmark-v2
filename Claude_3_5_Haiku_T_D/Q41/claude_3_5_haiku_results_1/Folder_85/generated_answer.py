def identical_elements(list1, list2):
    return set((x for x in set(list1[6:9]) & set(list2[6:9]) if x in list1[6:9] and x in list2[6:9]))