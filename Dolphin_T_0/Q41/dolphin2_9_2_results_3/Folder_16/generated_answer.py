def identical_elements(list1, list2):
    indices = range(33, 37)
    set1 = set((list1[i] for i in indices))
    set2 = set((list2[i] for i in indices))
    return set1.intersection(set2)