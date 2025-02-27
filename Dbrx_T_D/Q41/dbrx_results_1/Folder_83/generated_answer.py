def identical_elements(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)) or len(list1) != len(list2) or len(list1) < 180:
        return set()
    return set(list1[90:201]).intersection(list2[90:201])