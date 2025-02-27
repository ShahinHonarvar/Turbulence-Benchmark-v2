def identical_elements(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list) or len(list1) != len(list2) or (len(list1) < 1) or (len(list1) > 8):
        return set()
    else:
        return set(list1) & set(list2)