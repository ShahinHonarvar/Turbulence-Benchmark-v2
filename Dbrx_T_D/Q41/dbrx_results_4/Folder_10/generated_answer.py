def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 25 or len(list1) < 59:
        return set()
    return set(list1[25:60]).intersection(list2[25:60])