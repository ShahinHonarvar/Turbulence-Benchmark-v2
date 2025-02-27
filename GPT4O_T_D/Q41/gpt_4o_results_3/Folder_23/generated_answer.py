def identical_elements(list1, list2):
    if len(list1) <= 71 or len(list2) <= 71:
        return set()
    return set(list1[52:72]).intersection(list2[52:72])