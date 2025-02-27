def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set(list1[42:69]).intersection(list2[42:69])