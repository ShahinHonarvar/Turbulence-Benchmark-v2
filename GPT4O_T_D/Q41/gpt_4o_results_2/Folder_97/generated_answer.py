def identical_elements(list1, list2):
    if len(list1) < 81 or len(list2) < 81:
        return set()
    return set(list1[40:81]).intersection(set(list2[40:81]))