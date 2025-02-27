def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 15 or len(list2) < 15:
        return set()
    return set(list1[15:40]).intersection(list2[15:40])