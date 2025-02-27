def identical_elements(list1, list2):
    if len(list1) < 55 or len(list2) < 55:
        return set()
    return set(list1[50:55]).intersection(list2[50:55])