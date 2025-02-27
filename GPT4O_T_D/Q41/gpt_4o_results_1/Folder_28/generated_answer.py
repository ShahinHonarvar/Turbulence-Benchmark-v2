def identical_elements(list1, list2):
    if len(list1) < 64 or len(list2) < 64:
        return set()
    return set(list1[62:64]).intersection(list2[62:64])