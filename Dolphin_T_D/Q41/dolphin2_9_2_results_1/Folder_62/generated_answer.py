def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must have the same size')
    set1 = set((ele for ele in list1[91:100]))
    set2 = set((ele for ele in list2[91:100]))
    return set1 & set2