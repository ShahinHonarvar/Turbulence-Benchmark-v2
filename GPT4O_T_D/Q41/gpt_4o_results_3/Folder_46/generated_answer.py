def identical_elements(list1, list2):
    if len(list1) < 88 or len(list2) < 88:
        return set()
    return set(list1[30:88]).intersection(list2[30:88])