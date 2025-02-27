def identical_elements(list1, list2):
    if len(list1) < 67 or len(list2) < 67:
        return set()
    return set(list1[56:67]).intersection(set(list2[56:67]))