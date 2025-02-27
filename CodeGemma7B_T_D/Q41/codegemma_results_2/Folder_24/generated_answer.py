def identical_elements(list1, list2):
    return set((a for a, b in zip(list1[74:96], list2[74:96]) if a == b))