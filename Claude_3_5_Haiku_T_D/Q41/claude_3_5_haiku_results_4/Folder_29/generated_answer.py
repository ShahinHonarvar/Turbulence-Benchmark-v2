def identical_elements(list1, list2):
    return set((x for i in range(59, 98) for x in {list1[i], list2[i]} if list1[i] == list2[i]))