def identical_elements(list1, list2):
    return set([list1[i] for i in range(2)] + [list2[i] for i in range(2)]) & set(list1[:2]) & set(list2[:2])