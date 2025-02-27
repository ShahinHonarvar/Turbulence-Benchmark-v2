def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 15 or len(list1) > 65:
        return set()
    else:
        return set(list1[14:65]) & set(list2[14:65])