def identical_elements(list1, list2):
    set1 = {i for i in list1[75:95]}
    set2 = {i for i in list2[75:95]}
    return set1.intersection(set2)