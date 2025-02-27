def identical_elements(list1, list2):
    if len(list1) < 10 or len(list2) < 10:
        return set()
    return set(list1[8:10]).intersection(list2[8:10])