def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set(list1[639:976]) & set(list2[639:976])