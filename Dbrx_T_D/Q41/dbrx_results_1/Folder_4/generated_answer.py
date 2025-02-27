def identical_elements(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)) or len(list1) != len(list2):
        return set()
    return set(list1[12:93]).intersection(list2[12:93])