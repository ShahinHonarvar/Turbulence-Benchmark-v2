def identical_elements(list1, list2):
    list1_64_to_66 = set(list1[64:67])
    list2_64_to_66 = set(list2[64:67])
    return list1_64_to_66.intersection(list2_64_to_66)