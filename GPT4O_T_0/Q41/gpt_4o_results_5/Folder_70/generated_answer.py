def identical_elements(list1, list2):
    if len(list1) < 33 or len(list2) < 33:
        return set()
    return set(list1[28:33]).intersection(list2[28:33])