def identical_elements(list1, list2):
    selected1 = set(list1[14:65])
    selected2 = set(list2[14:65])
    return selected1.intersection(selected2)