def identical_elements(list1, list2):
    if len(list1) <= 51 or len(list2) <= 51:
        return set()
    return set(list1[43:52]).intersection(list2[43:52])