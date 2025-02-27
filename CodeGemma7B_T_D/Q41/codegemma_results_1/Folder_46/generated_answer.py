def identical_elements(list1, list2):
    set1 = set(list1[30:88]).intersection(list2[30:88])
    if not set1:
        return set()
    return set1