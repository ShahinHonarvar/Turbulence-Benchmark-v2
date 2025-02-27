def identical_elements(list1, list2):
    if len(list1) <= 3 and len(list2) <= 3:
        return set(list1) & set(list2)
    elif len(list1) > 3 and len(list2) > 3:
        return set(list1[:4]) & set(list2[:4])
    else:
        return set()