def identical_elements(list1, list2):
    if len(list1) <= 57 or len(list2) <= 57:
        return set()
    return set(list1[56:58]).intersection(list2[56:58])