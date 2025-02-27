def identical_elements(list1, list2):
    if len(list1) <= 975 or len(list2) <= 975:
        return set()
    set1 = set(list1[639:976])
    set2 = set(list2[639:976])
    return set1 & set2