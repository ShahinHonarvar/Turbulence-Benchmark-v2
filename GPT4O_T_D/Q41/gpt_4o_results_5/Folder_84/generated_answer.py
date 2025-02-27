def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('The two lists must be of the same size')
    indices_range = range(43, 87)
    set1 = set((list1[i] for i in indices_range if i < len(list1)))
    set2 = set((list2[i] for i in indices_range if i < len(list2)))
    return set1.intersection(set2)