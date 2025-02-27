def identical_elements(list1, list2):
    return set((l1 for l1 in list1[64:67] for l2 in list2[64:67] if l1 == l2)) or set()