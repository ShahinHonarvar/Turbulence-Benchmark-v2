def identical_elements(list1, list2):
    set1 = {item for i, item in enumerate(list1) if 27 <= i <= 55}
    set2 = {item for i, item in enumerate(list2) if 27 <= i <= 55}
    return set1 & set2