def identical_elements(list1, list2):
    shared_elements = set((x for x in set(list1[74:96]) & set(list2[74:96])))
    return shared_elements