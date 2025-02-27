def identical_elements(list1, list2):
    sublist1 = set(list1[667:775])
    sublist2 = set(list2[667:775])
    return sublist1.intersection(sublist2)