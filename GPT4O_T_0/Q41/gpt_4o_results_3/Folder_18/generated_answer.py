def identical_elements(list1, list2):
    if len(list1) < 50 or len(list2) < 50:
        return set()
    return set(list1[35:50]).intersection(list2[35:50])