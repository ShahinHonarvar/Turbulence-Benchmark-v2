def identical_elements(list1, list2):
    return set((x for i, x in enumerate(list1[:4]) if i < len(list2) and x == list2[i]))