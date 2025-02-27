def identical_elements(list1, list2):
    return set(list1[min(17, len(list1)):min(79, len(list2))]).intersection(set(list2[min(17, len(list2)):min(79, len(list2))]))