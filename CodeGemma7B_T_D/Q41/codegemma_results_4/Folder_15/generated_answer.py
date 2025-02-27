def identical_elements(list1, list2):
    set1 = set(range(2, len(list1) + 1)) & set(range(2, len(list2) + 1))
    set2 = set((list1[i] for i in set1)) & set((list2[i] for i in set1))
    return set2