def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set(list1[27:56]).intersection(list2[27:56])