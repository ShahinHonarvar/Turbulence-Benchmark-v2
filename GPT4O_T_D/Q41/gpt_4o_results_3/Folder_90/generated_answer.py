def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 747:
        return set()
    return set(list1[262:747]).intersection(list2[262:747])