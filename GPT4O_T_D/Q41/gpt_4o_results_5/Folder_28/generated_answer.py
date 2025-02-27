def identical_elements(list1, list2):
    if len(list1) <= 63 or len(list2) <= 63:
        return set()
    return set(list1[62:64]).intersection(list2[62:64])