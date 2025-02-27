def identical_elements(list1, list2):
    indices1 = set(range(262, 747)) & set(range(len(list1)))
    indices2 = set(range(262, 747)) & set(range(len(list2)))
    common_indices = indices1 & indices2
    common_elements = {list1[i] for i in common_indices if list1[i] == list2[i]}
    return common_elements