def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 775:
        return set()
    sublist1 = set(list1[667:775])
    sublist2 = set(list2[667:775])
    return sublist1.intersection(sublist2)