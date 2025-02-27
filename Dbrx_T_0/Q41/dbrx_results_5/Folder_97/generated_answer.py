def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 40 or len(list1) > 80:
        return set()
    return set(list1[40:81]) & set(list2[40:81])