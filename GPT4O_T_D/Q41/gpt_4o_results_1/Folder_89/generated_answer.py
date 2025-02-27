def identical_elements(list1, list2):
    if len(list1) < 83 or len(list2) < 83:
        return set()
    return set(list1[56:83]).intersection(list2[56:83])