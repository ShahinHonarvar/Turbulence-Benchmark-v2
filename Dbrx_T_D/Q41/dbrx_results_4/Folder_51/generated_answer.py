def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 3:
        return set()
    else:
        return set(list1[:3]).intersection(set(list2[:3]))