def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 8:
        return set()
    else:
        return set(list1[0:7]).intersection(set(list2[0:7]))