def identical_elements(list1, list2):
    if len(list1) < 47 or len(list2) < 47:
        return set()
    return set(list1[36:47]).intersection(list2[36:47])