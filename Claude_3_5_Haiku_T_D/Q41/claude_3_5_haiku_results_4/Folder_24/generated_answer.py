def identical_elements(list1, list2):
    return set((x for x in set(list1[74:96] + list2[74:96]) if x in list1[74:96] and x in list2[74:96]))