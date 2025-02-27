def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 18 or len(list2) < 18:
        return set()
    else:
        return set(list1[17:79]).intersection(list2[17:79])