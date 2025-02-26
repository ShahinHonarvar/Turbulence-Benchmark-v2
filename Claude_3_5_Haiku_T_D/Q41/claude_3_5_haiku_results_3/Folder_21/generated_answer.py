def identical_elements(list1, list2):
    if len(list1) <= 975 or len(list2) <= 975:
        return set()
    common_elements = set(list1[639:976]) & set(list2[639:976])
    return common_elements