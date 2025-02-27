def identical_elements(list1, list2):
    common_elements = set(list1[20:201]).intersection(list2[20:201])
    if not common_elements:
        return set()
    return common_elements